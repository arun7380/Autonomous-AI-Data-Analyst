from typing import List, Dict, Any, Optional
from pydantic import BaseModel


class DashboardWidget(BaseModel):
    widget_id: str
    widget_type: str  # 'kpi', 'chart', 'table', 'text'
    title: str
    grid_position: Dict[str, int]  # x, y, w, h
    content_payload: Dict[str, Any]


class DashboardResponse(BaseModel):
    dataset_id: str
    dashboard_title: str
    kpis: List[Dict[str, Any]]
    widgets: List[DashboardWidget]
    key_takeaways: List[str]
