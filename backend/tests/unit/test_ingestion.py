import pytest
import os
import polars as pl
from app.services.ingestion_service import IngestionService


def test_supported_extensions():
    assert ".csv" in IngestionService.SUPPORTED_EXTENSIONS
    assert ".parquet" in IngestionService.SUPPORTED_EXTENSIONS
    assert ".xlsx" in IngestionService.SUPPORTED_EXTENSIONS


def test_csv_ingestion(tmp_path):
    # Create temporary CSV file
    df = pl.DataFrame({"a": [1, 2, 3], "b": ["x", "y", "z"]})
    file_path = os.path.join(tmp_path, "sample.csv")
    df.write_csv(file_path)

    row_cnt, col_cnt, schema = IngestionService.process_file_upload("sample.csv", file_path)
    assert row_cnt == 3
    assert col_cnt == 2
    assert "a" in schema
    assert "b" in schema
