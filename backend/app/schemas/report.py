from typing import Optional
from pydantic import BaseModel


class ReportGenerateRequest(BaseModel):
    dataset_id: str
    format: str = "pdf"  # 'pdf', 'html', 'markdown'
    include_eda: bool = True
    include_ml: bool = True
    custom_title: Optional[str] = None


class ReportGenerateResponse(BaseModel):
    report_id: str
    download_url: str
    format: str
    file_size_bytes: int
