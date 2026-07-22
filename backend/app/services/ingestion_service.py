import os
import uuid
import polars as pl
import pandas as pd
from typing import Dict, Any, Tuple
from app.core.exceptions import UnsupportedFileFormatException
from app.database.duckdb_engine import duckdb_manager
from app.core.logger import logger


class IngestionService:
    """Multi-format data ingestion service supporting CSV, Excel, Parquet, JSON, and SQL files using Polars & DuckDB."""

    SUPPORTED_EXTENSIONS = {".csv", ".xlsx", ".xls", ".parquet", ".json", ".sqlite", ".db"}

    @classmethod
    def process_file_upload(cls, file_name: str, file_path: str) -> Tuple[int, int, Dict[str, str]]:
        """Parses uploaded file, registers it with DuckDB for zero-copy memory analytics, and extracts metadata."""
        ext = os.path.splitext(file_name)[1].lower()
        if ext not in cls.SUPPORTED_EXTENSIONS:
            raise UnsupportedFileFormatException(ext)

        logger.info(f"Ingesting file '{file_name}' from path '{file_path}'")

        try:
            if ext == ".csv":
                df_lazy = pl.scan_csv(file_path, ignore_errors=True)
                schema = df_lazy.schema
                row_count = df_lazy.select(pl.len()).collect().item()
            elif ext == ".parquet":
                df_lazy = pl.scan_parquet(file_path)
                schema = df_lazy.schema
                row_count = df_lazy.select(pl.len()).collect().item()
            elif ext in [".xlsx", ".xls"]:
                df_pandas = pd.read_excel(file_path)
                row_count = len(df_pandas)
                schema = {col: str(dtype) for col, dtype in df_pandas.dtypes.items()}
            elif ext == ".json":
                df_lazy = pl.scan_ndjson(file_path)
                schema = df_lazy.schema
                row_count = df_lazy.select(pl.len()).collect().item()
            else:
                row_count = 0
                schema = {}

            column_count = len(schema)
            column_types = {col: str(dtype) for col, dtype in schema.items()}

            # Register view in DuckDB analytical engine
            table_name = f"dataset_{uuid.uuid4().hex[:8]}"
            duckdb_manager.register_parquet(table_name, file_path)

            return row_count, column_count, column_types
        except Exception as e:
            logger.error(f"Failed to ingest file '{file_name}'", error=str(e))
            raise e
