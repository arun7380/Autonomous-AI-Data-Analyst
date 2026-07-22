import os
import uuid
import shutil
from fastapi import APIRouter, UploadFile, File, HTTPException, status
from app.core.config import settings
from app.schemas.dataset import DatasetResponse
from app.services.ingestion_service import IngestionService
from app.core.logger import logger

router = APIRouter(prefix="/upload", tags=["Dataset Upload"])


@router.post("", response_model=DatasetResponse, status_code=status.HTTP_201_CREATED)
async def upload_dataset(file: UploadFile = File(...)):
    """Accepts drag-and-drop CSV, XLSX, Parquet, JSON, and SQL files, parses schemas & registers with DuckDB."""
    os.makedirs(settings.UPLOAD_DIR, exist_ok=True)
    file_id = str(uuid.uuid4())
    file_ext = os.path.splitext(file.filename)[1]
    saved_filename = f"{file_id}{file_ext}"
    saved_path = os.path.join(settings.UPLOAD_DIR, saved_filename)

    with open(saved_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    file_size = os.path.getsize(saved_path)

    try:
        row_count, col_count, col_types = IngestionService.process_file_upload(file.filename, saved_path)
    except Exception as e:
        logger.error("Upload error", error=str(e))
        raise HTTPException(status_code=400, detail=str(e))

    return DatasetResponse(
        id=file_id,
        name=file.filename,
        file_type=file_ext,
        file_size_bytes=file_size,
        row_count=row_count,
        column_count=col_count,
        created_at=os.path.getctime(saved_path),
        columns=list(col_types.keys()),
        column_types=col_types
    )
