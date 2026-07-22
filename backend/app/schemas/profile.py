from typing import List, Dict, Any, Optional
from pydantic import BaseModel


class ColumnSummary(BaseModel):
    name: str
    data_type: str
    semantic_type: str  # numerical, categorical, datetime, text, id
    missing_count: int
    missing_percentage: float
    unique_count: int
    mean: Optional[float] = None
    std: Optional[float] = None
    min: Optional[Any] = None
    max: Optional[Any] = None
    skewness: Optional[float] = None


class ProfileRequest(BaseModel):
    dataset_id: str


class ProfileResponse(BaseModel):
    dataset_id: str
    total_rows: int
    total_columns: int
    duplicate_rows: int
    columns_summary: List[ColumnSummary]
    correlation_matrix: Optional[Dict[str, Dict[str, float]]] = None
    quality_score: float  # 0.0 to 100.0 score
