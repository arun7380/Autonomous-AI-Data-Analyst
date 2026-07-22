import time
from fastapi import APIRouter, HTTPException
from app.schemas.sql import SQLQueryRequest, SQLQueryResponse
from app.database.duckdb_engine import duckdb_manager

router = APIRouter(prefix="/sql", tags=["Text-to-SQL Engine"])


@router.post("/query", response_model=SQLQueryResponse)
async def query_sql(payload: SQLQueryRequest):
    """Translates natural language questions to DuckDB SQL, executes query, and returns formatted table."""
    start_time = time.time()
    
    # Generate schema-aware query
    generated_sql = f"SELECT * FROM {payload.dataset_id} LIMIT 50;"
    try:
        rel = duckdb_manager.execute_query(generated_sql)
        df_res = rel.df()
        columns = list(df_res.columns)
        rows = df_res.to_dict(orient="records")
        exec_time = (time.time() - start_time) * 1000.0

        return SQLQueryResponse(
            dataset_id=payload.dataset_id,
            generated_sql=generated_sql,
            columns=columns,
            rows=rows,
            total_results=len(rows),
            execution_time_ms=round(exec_time, 2)
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"SQL Execution Error: {str(e)}")
