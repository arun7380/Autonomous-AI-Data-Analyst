import duckdb
from typing import Optional
from app.core.config import settings
from app.core.logger import logger


class DuckDBEngineManager:
    """Manages high-performance DuckDB connections for fast SQL query execution over large datasets."""
    
    _instance: Optional["DuckDBEngineManager"] = None

    def __init__(self):
        self.conn = duckdb.connect(database=settings.DUCKDB_PATH, read_only=False)
        self.conn.execute("SET threads TO 8;")
        self.conn.execute("SET memory_limit = '4GB';")
        logger.info("DuckDB engine initialized successfully.")

    @classmethod
    def get_instance(cls) -> "DuckDBEngineManager":
        if cls._instance is None:
            cls._instance = DuckDBEngineManager()
        return cls._instance

    def execute_query(self, sql_query: str) -> duckdb.DuckDBPyRelation:
        """Executes SQL query and returns relation."""
        try:
            return self.conn.sql(sql_query)
        except Exception as e:
            logger.error("DuckDB Query Execution Error", error=str(e), sql=sql_query)
            raise e

    def register_parquet(self, table_name: str, file_path: str):
        """Registers a Parquet or CSV file directly as a DuckDB view without loading entirely into RAM."""
        query = f"CREATE OR REPLACE VIEW {table_name} AS SELECT * FROM read_auto('{file_path}');"
        self.conn.execute(query)
        logger.info(f"Registered view '{table_name}' pointing to file '{file_path}'")


duckdb_manager = DuckDBEngineManager.get_instance()
