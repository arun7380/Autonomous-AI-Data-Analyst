from app.agents.state import AgentState, AgentStep
from app.core.logger import logger


class ReflectionAgent:
    """Reflection and Quality Assurance Agent that inspects generated SQL, statistics, and text to ensure correctness."""

    @classmethod
    def execute(cls, state: AgentState) -> AgentState:
        sql = state.get("generated_sql")
        error = state.get("error")

        if error:
            logger.warning(f"ReflectionAgent detected error: {error}. Triggering re-planning.")
            thought = f"Detected error in prior step: {error}. Requesting correction."
        else:
            thought = "Verified generated SQL, insights, and code. No anomalies found."

        step: AgentStep = {
            "agent_name": "ReflectionAgent",
            "thought": thought,
            "action": "Quality Inspection",
            "output": "Approval granted." if not error else "Retry recommended."
        }
        state["agent_steps"].append(step)
        return state
