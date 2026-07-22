from datetime import datetime
from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field


class DatasetBase(BaseModel):
    name: str
    file_type: str
    file_size_bytes: int
    row_count: int
    column_count: int


class DatasetCreate(DatasetBase):
    storage_path: str


class DatasetResponse(DatasetBase):
    id: str
    created_at: datetime
    columns: List[str]
    column_types: Dict[str, str]

    class Config:
        from_attributes = True


class DatasetPreviewResponse(BaseModel):
    dataset_id: str
    columns: List[str]
    sample_data: List[Dict[str, Any]]
    total_rows: int
