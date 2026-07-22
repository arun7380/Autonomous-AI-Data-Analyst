from typing import Dict, Any, List, Optional
from pydantic import BaseModel


class MLTrainRequest(BaseModel):
    dataset_id: str
    target_column: str
    problem_type: Optional[str] = "auto"  # 'auto', 'classification', 'regression', 'clustering'
    time_budget_sec: int = 120


class MLTrainResponse(BaseModel):
    model_id: str
    best_algorithm: str
    problem_type: str
    metrics: Dict[str, float]  # Accuracy, Precision, Recall, F1, ROC_AUC, RMSE, R2
    feature_importance: Dict[str, float]
    shap_values_available: bool
    mlflow_run_id: str


class MLPredictRequest(BaseModel):
    model_id: str
    input_features: Dict[str, Any]


class MLPredictResponse(BaseModel):
    prediction: Any
    prediction_probability: Optional[float] = None
    shap_explanation: Optional[Dict[str, float]] = None
