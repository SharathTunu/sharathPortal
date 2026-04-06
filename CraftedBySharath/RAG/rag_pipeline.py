"""
In-process RAG for the portfolio chatbot (LangChain + FAISS).
Supports Groq (default) and Ollama as LLM providers, controlled by RAG_LLM_PROVIDER.
Paths and model names come from Django settings.
"""
import glob
import threading
from pathlib import Path
from typing import Any, Optional, Tuple

from django.conf import settings

from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferWindowMemory
from langchain.prompts import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

vectorstore: Any = None
qa_chain: Any = None
embeddings: Any = None
_init_lock = threading.Lock()
_ready: bool = False


def _docs_dir() -> Path:
    return Path(settings.RAG_DOCS_DIR)


def _index_dir() -> Path:
    return Path(settings.RAG_INDEX_DIR)


def _system_prompt() -> str:
    name = getattr(settings, "RAG_PORTFOLIO_NAME", "Sharath")
    return f"""You are a helpful AI assistant representing {name}'s professional portfolio.
    Your job is to answer questions about {name}'s background, skills, projects, and experience
    using the context provided below. The context contains factual information extracted from {name}'s
    documents — trust it fully and use it to answer questions directly and completely.
    
    Rules:
    - ALWAYS use the context below to answer. It contains the information you need.
    - Speak in the third person about {name} (e.g., "{name} trained a SigLIP model...").
    - If the question asks for a list, return a complete list using the context — do not summarise or truncate.
    - If the question asks for metrics or numbers, include them exactly as they appear in the context.
    - Only say you don't know if the topic is genuinely absent from the context.
    - Be warm, professional, and direct. Match the length of the answer to the complexity of the question.
    - When the question is a simple greeting, respond with a warm welcome and ask the user to ask a question about {name}'s background, skills, projects, and experience.
    
    Context:
    {{context}}
    
    Chat History:
    {{chat_history}}
    
    Question: {{question}}
    Answer:"""


def get_embeddings():
    global embeddings
    if embeddings is None:
        model = getattr(
            settings,
            "RAG_EMBED_MODEL",
            "sentence-transformers/all-MiniLM-L6-v2",
        )
        embeddings = HuggingFaceEmbeddings(
            model_name=model,
            model_kwargs={"device": "cpu"},
            encode_kwargs={"normalize_embeddings": True},
        )
    return embeddings


def load_documents() -> list:
    docs_dir = _docs_dir()
    docs = []
    pattern = str(docs_dir / "**" / "*")
    for path in glob.glob(pattern, recursive=True):
        if not Path(path).is_file():
            continue
        try:
            if path.endswith(".pdf"):
                docs.extend(PyPDFLoader(path).load())
            elif path.endswith((".txt", ".md")):
                docs.extend(TextLoader(path, encoding="utf-8").load())
        except Exception:
            continue
    return docs


def _chunk_settings():
    return (
        getattr(settings, "RAG_CHUNK_SIZE", 500),
        getattr(settings, "RAG_CHUNK_OVERLAP", 60),
        getattr(settings, "RAG_TOP_K", 4),
    )


def build_index() -> None:
    global vectorstore, qa_chain

    chunk_size, chunk_overlap, top_k = _chunk_settings()
    documents = load_documents()
    if not documents:
        raise FileNotFoundError(
            f"No PDF/TXT/MD files found under '{_docs_dir()}'. Add documents and try again."
        )

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ". ", " ", ""],
    )
    chunks = splitter.split_documents(documents)
    idx = _index_dir()
    idx.mkdir(parents=True, exist_ok=True)

    vectorstore = FAISS.from_documents(chunks, get_embeddings())
    vectorstore.save_local(str(idx))
    _init_chain(top_k)


def load_index() -> None:
    global vectorstore
    _, _, top_k = _chunk_settings()
    idx = _index_dir()
    vectorstore = FAISS.load_local(
        str(idx),
        get_embeddings(),
        allow_dangerous_deserialization=True,
    )
    _init_chain(top_k)


def _build_llm():
    provider = getattr(settings, "RAG_LLM_PROVIDER", "groq")

    if provider == "ollama":
        from langchain_ollama import ChatOllama
        return ChatOllama(
            model=getattr(settings, "RAG_OLLAMA_MODEL", "llama3.2"),
            base_url=getattr(settings, "RAG_OLLAMA_BASE_URL", "http://127.0.0.1:11434"),
            temperature=0.3,
            num_predict=512,
        )

    # Default: groq
    from langchain_groq import ChatGroq
    api_key = getattr(settings, "RAG_GROQ_API_KEY", "")
    if not api_key:
        raise ValueError("RAG_GROQ_API_KEY is not set. Add it to your environment variables.")
    return ChatGroq(
        api_key=api_key,
        model=getattr(settings, "RAG_GROQ_MODEL", "llama-3.3-70b-versatile"),
        temperature=0.3,
        max_tokens=512,
    )


def _init_chain(top_k: int) -> None:
    global qa_chain

    prompt_text = _system_prompt()
    llm = _build_llm()

    memory = ConversationBufferWindowMemory(
        memory_key="chat_history",
        return_messages=True,
        output_key="answer",
        k=6,
    )

    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(search_kwargs={"k": top_k}),
        memory=memory,
        combine_docs_chain_kwargs={
            "prompt": PromptTemplate(
                input_variables=["context", "chat_history", "question"],
                template=prompt_text,
            )
        },
        return_source_documents=False,
        verbose=False,
    )


def ensure_rag_ready() -> Optional[str]:
    """
    Load or build the index and chain. Returns an error message string if unavailable.
    """
    global _ready
    with _init_lock:
        if _ready and qa_chain is not None:
            return None

        _docs_dir().mkdir(parents=True, exist_ok=True)

        if _index_dir().exists() and any(_index_dir().iterdir()):
            try:
                load_index()
                _ready = True
                return None
            except Exception as e:
                return f"Could not load RAG index: {e}"

        try:
            build_index()
            _ready = True
            return None
        except FileNotFoundError as e:
            return str(e)
        except Exception as e:
            return f"RAG setup failed: {e}"


def invoke_chat(question: str) -> Tuple[Optional[str], Optional[str]]:
    """
    Run the QA chain. Returns (answer, error). One of the two is set.
    """
    err = ensure_rag_ready()
    if err:
        return None, err
    if qa_chain is None:
        return None, "RAG index is not ready."

    try:
        result = qa_chain.invoke({"question": question})
        answer = result.get("answer", "I'm not sure — could you rephrase?")
        return answer, None
    except Exception:
        return None, "Something went wrong. Check your LLM provider config and try again."


def ingest_from_docs() -> None:
    """Rebuild the FAISS index from RAG_DOCS_DIR (for management command)."""
    global vectorstore, qa_chain, _ready
    with _init_lock:
        vectorstore = None
        qa_chain = None
        _ready = False
        build_index()
        _ready = True
