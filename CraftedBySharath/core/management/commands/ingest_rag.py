from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Rebuild the FAISS index from RAG_DOCS_DIR (see settings)."

    def handle(self, *args, **options):
        try:
            from RAG.rag_pipeline import ingest_from_docs
        except ImportError as exc:
            raise CommandError(
                "RAG dependencies missing. Install with: pip install -r requirements.txt"
            ) from exc

        try:
            ingest_from_docs()
        except Exception as exc:
            raise CommandError(str(exc)) from exc

        self.stdout.write(self.style.SUCCESS("RAG index rebuilt successfully."))
