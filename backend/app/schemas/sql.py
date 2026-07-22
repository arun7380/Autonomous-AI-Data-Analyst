from typing import List, Dict, Any, Optional
from pydantic import BaseModel


class SQLQueryRequest(BaseModel):
    dataset_id: str
    natural_language_query: str


class SQLQueryResponse(BaseModel):
    dataset_id: str
    generated_sql: str
    columns: List[str]
    rows: List[Dict[str, Any]]
    total_results: int
    execution_time_ms: float
    recommended_chart: Optional[Dict[str, Any]] = None
