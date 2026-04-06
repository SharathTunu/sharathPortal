# Portfolio RAG

Source documents, optional FAISS index cache, and the LangChain pipeline used by the Django chat modal (`/api/rag/chat/`).

## Layout

| Path | Purpose |
|------|---------|
| `docs/` | PDF, TXT, and Markdown files to retrieve from (add your resume and notes here). |
| `faiss_index/` | Created automatically when you ingest or on first chat; safe to delete to force a rebuild. |
| `rag_pipeline.py` | In-process RAG: embeddings, FAISS, Ollama via LangChain. |
| `chat-widget.html` | Standalone widget snippet (the site uses the Bootstrap modal in `core/templates` instead). |

## Setup

1. Install project dependencies from the `CraftedBySharath` folder: `pip install -r requirements.txt`
2. Install [Ollama](https://ollama.com) and pull a model (must match `RAG_OLLAMA_MODEL` in Django settings, default `llama3.2`). Run: `ollama pull llama3.2`
3. Put files under `docs/`.
4. From `CraftedBySharath`, run:

   ```bash
   python manage.py ingest_rag
   ```

   Or start the dev server and open the portfolio RAG tile — the index will build on first message if missing.

## Django settings

Paths and models are configured in `CraftedBySharath/settings.py` (`RAG_DOCS_DIR`, `RAG_INDEX_DIR`, `RAG_OLLAMA_*`, etc.). Override with environment variables if needed.
