from typing import List, Optional
from pydantic import BaseModel


class CleanRequest(BaseModel):
    dataset_id: str
    fill_missing_strategy: str = "auto"  # 'auto', 'mean', 'median', 'mode', 'drop'
    remove_duplicates: bool = True
    handle_outliers: bool = True
    outlier_method: str = "iqr"  # 'iqr' or 'zscore'
    standardize_columns: bool = True


class CleanResponse(BaseModel):
    cleaned_dataset_id: str
    original_rows: int
    cleaned_rows: int
    missing_values_filled: int
    duplicates_removed: int
    outliers_detected: int
    applied_transformations: List[str]
