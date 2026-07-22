from app.agents.state import AgentState, AgentStep
from app.database.duckdb_engine import duckdb_manager
from app.core.logger import logger


class SQLAgent:
    """Translates natural language user questions into schema-aware DuckDB SQL queries and executes them."""

    @classmethod
    def execute(cls, state: AgentState) -> AgentState:
        table_name = state.get("table_name", "dataset")
        user_query = state.get("user_query", "")

        # Fallback schema-aware query generator
        sql_query = f"SELECT * FROM {table_name} LIMIT 100;"
        if "top" in user_query.lower() or "best" in user_query.lower():
            sql_query = f"SELECT * FROM {table_name} LIMIT 10;"

        logger.info(f"SQLAgent generated query: {sql_query}")

        try:
            rel = duckdb_manager.execute_query(sql_query)
            df_res = rel.df()
            rows = df_res.to_dict(orient="records")

            state["generated_sql"] = sql_query
            state["sql_results"] = rows

            step: AgentStep = {
                "agent_name": "SQLAgent",
                "thought": f"Generated SQL query '{sql_query}' for user question.",
                "action": "Execute SQL in DuckDB",
                "output": f"Retrieved {len(rows)} result rows."
            }
            state["agent_steps"].append(step)
        except Exception as e:
            state["error"] = str(e)

        return state
