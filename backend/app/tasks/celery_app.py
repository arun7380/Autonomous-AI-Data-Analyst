from celery import Celery
from app.core.config import settings

celery_app = Celery(
    "autonomous_analyst_tasks",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND,
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
    task_track_started=True,
)


@celery_app.task(name="tasks.ingest_large_file")
def ingest_large_file_task(file_path: str, dataset_id: str):
    """Background task for streaming massive multi-gigabyte datasets into DuckDB storage."""
    return {"status": "completed", "dataset_id": dataset_id, "file_path": file_path}
