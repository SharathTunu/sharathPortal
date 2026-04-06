import json
from pathlib import Path

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST


SERVICE_CONTENT_MAP = {
    "ai_ml": {"title": "AI/ML", "filename": "ai_ml.md"},
    "visual_intelligence": {
        "title": "Visual Intelligence",
        "filename": "visual_intelligence.md",
    },
    "ml_ops": {"title": "ML OPS", "filename": "ml_ops.md"},
    "web_design": {"title": "Web Design", "filename": "web_design.md"},
}

ALLOWED_SERVICE_SECTIONS = frozenset(SERVICE_CONTENT_MAP.keys())
EXPERTISE_DIR = Path(__file__).resolve().parent / "Expertise"

# In production (DEBUG=False), videos live in STATIC_ROOT after collectstatic.
# In development, they live in core/static/.
_STATIC_ROOT = getattr(settings, "STATIC_ROOT", None)
_APP_STATIC = Path(__file__).resolve().parent / "static"
_VIDEOS_BASE = Path(_STATIC_ROOT) if _STATIC_ROOT and not settings.DEBUG else _APP_STATIC

CV_VIDEOS_DIR = _VIDEOS_BASE / "videos"
WEB_DESIGN_VIDEOS_DIR = _VIDEOS_BASE / "web_design"
_CV_VIDEO_EXT = frozenset({".mp4", ".webm", ".ogg", ".mov", ".m4v"})


def _list_demo_videos_in_dir(directory: Path):
    if not directory.is_dir():
        return []
    return sorted(
        p.name
        for p in directory.iterdir()
        if p.is_file()
        and p.suffix.lower() in _CV_VIDEO_EXT
        and not p.name.startswith(".")
    )

def _escape_html(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
        .replace("'", "&#x27;")
    )


def _inline_md_to_html(text: str) -> str:
    """
    Convert a small subset of markdown to safe HTML.
    Supported: **bold**, otherwise HTML-escaped.
    """
    escaped = _escape_html(text)
    # Convert bold after escaping to keep it safe.
    import re

    escaped = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", escaped)
    return escaped


def simple_markdown_to_html(markdown_text: str) -> str:
    """
    Convert a small subset of markdown to human-readable HTML.
    Supported:
    - Headings (#, ##, ...)
    - Unordered lists (- ...) with nested indentation
    - Inline **bold**
    """
    import re

    lines = markdown_text.splitlines()
    html_parts: list[str] = []
    ul_stack: list[int] = []
    li_open: list[bool] = []

    para_lines: list[str] = []

    def flush_paragraph() -> None:
        nonlocal para_lines
        if not para_lines:
            return
        text = " ".join(s.strip() for s in para_lines if s.strip())
        if text:
            html_parts.append(f"<p>{_inline_md_to_html(text)}</p>")
        para_lines = []

    def close_all_lists() -> None:
        nonlocal ul_stack, li_open
        flush_paragraph()
        while ul_stack:
            lvl = len(ul_stack) - 1
            if lvl < len(li_open) and li_open[lvl]:
                html_parts.append("</li>")
                li_open[lvl] = False
            html_parts.append("</ul>")
            ul_stack.pop()
            li_open.pop()

    heading_re = re.compile(r"^(#{1,6})\s+(.*)$")
    list_re = re.compile(r"^(\s*)-\s+(.*)$")

    for raw_line in lines:
        line = raw_line.rstrip("\n")
        if not line.strip():
            # Blank line ends paragraphs and (for simplicity) closes lists.
            flush_paragraph()
            close_all_lists()
            continue

        heading_match = heading_re.match(line)
        if heading_match:
            close_all_lists()
            level = len(heading_match.group(1))
            content = heading_match.group(2).strip()
            html_parts.append(f"<h{level}>{_inline_md_to_html(content)}</h{level}>")
            continue

        list_match = list_re.match(line)
        if list_match:
            if para_lines:
                flush_paragraph()

            leading_spaces = len(list_match.group(1).replace("\t", "  "))
            text = list_match.group(2).strip()
            level = leading_spaces // 2

            # Ensure our stacks can represent this nesting level.
            current_level = len(ul_stack) - 1
            if level > current_level:
                # Start nested lists inside the currently open <li>.
                # There should already be an open <li> at the previous level.
                while len(ul_stack) <= level:
                    html_parts.append("<ul>")
                    ul_stack.append(level)
                    li_open.append(False)
            elif level < current_level:
                # Close deeper lists.
                while len(ul_stack) > level + 1:
                    lvl = len(ul_stack) - 1
                    if lvl < len(li_open) and li_open[lvl]:
                        html_parts.append("</li>")
                        li_open[lvl] = False
                    html_parts.append("</ul>")
                    ul_stack.pop()
                    li_open.pop()

            # Close previous <li> at the same list level.
            if level < len(li_open) and li_open[level]:
                html_parts.append("</li>")
                li_open[level] = False

            html_parts.append(f"<li>{_inline_md_to_html(text)}")
            if level >= len(li_open):
                # Should not happen, but keeps the function safe.
                li_open.append(True)
            else:
                li_open[level] = True
            continue

        # Regular line -> paragraph text
        para_lines.append(line.strip())

    # Final flush
    flush_paragraph()
    close_all_lists()

    # Close any still-open <li> tags (close_all_lists should have handled it,
    # but keep it robust).
    while li_open:
        if li_open[-1]:
            html_parts.append("</li>")
        li_open.pop()

    return "\n".join(html_parts)


def home(request):
    ml_skills = {
        "PyTorch": "90",
        "DeepStream": "65",
        "NN-based training": "95"
    }
    web_skills = {
        "Django": "90",
        "FastAPI": "85",
        "Flask": "95"
    }
    languages = {
        "Python": "95",
        "C++": "95",
        "JavaScript": "75",
        "bash": "85",
        "git-sourceControl": "90",
        "SQL": "70"
    }
    skill_groups = [ml_skills, web_skills]
    data = {
        "skill_groups": skill_groups,
        "languages": languages,
        "cv_videos": _list_demo_videos_in_dir(CV_VIDEOS_DIR),
        "web_design_videos": _list_demo_videos_in_dir(WEB_DESIGN_VIDEOS_DIR),
    }
    return render(request, "core/home.html", data)


@require_POST
def service_click(request):
    try:
        payload = json.loads(request.body.decode("utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError):
        return JsonResponse({"ok": False, "error": "invalid json"}, status=400)
    section = payload.get("section")
    if not isinstance(section, str) or section not in ALLOWED_SERVICE_SECTIONS:
        return JsonResponse({"ok": False, "error": "invalid section"}, status=400)
    spec = SERVICE_CONTENT_MAP.get(section)
    if not spec:
        return JsonResponse({"ok": False, "error": "invalid section"}, status=400)

    md_path = EXPERTISE_DIR / spec["filename"]
    try:
        markdown_text = md_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return JsonResponse({"ok": False, "error": "content not found"}, status=404)

    # Avoid duplicating the popup title: the markdown files start with a `# ...`
    # line, while the modal header already shows the service name.
    lines = markdown_text.splitlines()
    i = 0
    while i < len(lines) and not lines[i].strip():
        i += 1
    if i < len(lines) and lines[i].lstrip().startswith("#"):
        i += 1
        while i < len(lines) and not lines[i].strip():
            i += 1
    markdown_text = "\n".join(lines[i:])

    return JsonResponse(
        {
            "ok": True,
            "section": section,
            "title": spec["title"],
            "markdown": markdown_text,
            "html": simple_markdown_to_html(markdown_text),
        }
    )


@require_POST
def rag_chat(request):
    """
    Portfolio RAG chat (in-process LangChain + FAISS + Ollama).
    Expects JSON: {"message": "..."}
    """
    try:
        from RAG.rag_pipeline import invoke_chat
    except ImportError as exc:
        return JsonResponse(
            {
                "ok": False,
                "error": (
                    "RAG dependencies are not installed. "
                    f"Run: pip install -r requirements.txt ({exc})"
                ),
            },
            status=503,
        )

    try:
        payload = json.loads(request.body.decode("utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError):
        return JsonResponse({"ok": False, "error": "invalid json"}, status=400)

    message = (payload.get("message") or "").strip()
    if not message:
        return JsonResponse({"ok": False, "error": "No message provided."}, status=400)

    answer, err = invoke_chat(message)
    if err:
        return JsonResponse({"ok": False, "error": err}, status=503)
    return JsonResponse({"ok": True, "answer": answer})

