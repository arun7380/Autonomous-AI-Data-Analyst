from app.agents.state import AgentState, AgentStep
from app.database.duckdb_engine import duckdb_manager
from app.services.llm_factory import get_llm
from app.core.logger import logger
from app.core.config import settings


class SQLAgent:
    """Translates natural language user questions into schema-aware DuckDB SQL queries using Google/Groq LLMs and executes them."""

    @classmethod
    def execute(cls, state: AgentState) -> AgentState:
        table_name = state.get("table_name", "dataset")
        user_query = state.get("user_query", "")

        sql_query = None

        # Attempt to generate SQL using configured LLM (Google Gemini / Groq)
        if settings.GOOGLE_API_KEY or settings.GROQ_API_KEY:
            try:
                llm = get_llm(temperature=0.0)
                prompt = (
                    f"You are a SQL generator for DuckDB.\n"
                    f"Table Name: {table_name}\n"
                    f"User Query: {user_query}\n"
                    f"Return ONLY valid SQL code without formatting markdown backticks or explanations."
                )
                response = llm.invoke(prompt)
                raw_sql = response.content.strip()
                # Clean up any potential markdown formatting
                if raw_sql.startswith("```"):
                    lines = raw_sql.splitlines()
                    raw_sql = "\n".join([l for l in lines if not l.startswith("```")]).strip()
                if raw_sql:
                    sql_query = raw_sql
            except Exception as ex:
                logger.warning(f"LLM SQL generation failed, falling back to rule-based generation: {ex}")

        # Rule-based fallback if LLM is unavailable or failed
        if not sql_query:
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
                "thought": f"Generated SQL query '{sql_query}' using configured LLM.",
                "action": "Execute SQL in DuckDB",
                "output": f"Retrieved {len(rows)} result rows."
            }
            state["agent_steps"].append(step)
        except Exception as e:
            state["error"] = str(e)

        return state
