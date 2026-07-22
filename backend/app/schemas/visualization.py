from typing import Dict, Any, Optional, List
from pydantic import BaseModel


class VisualizationRequest(BaseModel):
    dataset_id: str
    chart_type: str  # 'histogram', 'boxplot', 'scatter', 'heatmap', 'violin', 'line', 'bar'
    x_column: str
    y_column: Optional[str] = None
    color_by: Optional[str] = None
    title: Optional[str] = None


class VisualizationResponse(BaseModel):
    dataset_id: str
    chart_type: str
    plotly_spec: Dict[str, Any]
    summary_insight: str
