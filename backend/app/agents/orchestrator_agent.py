from app.agents.state import AgentState, AgentStep
from app.core.logger import logger


class OrchestratorAgent:
    """Master Orchestrator Agent responsible for intent classification and routing execution across sub-agents."""

    @classmethod
    def execute(cls, state: AgentState) -> AgentState:
        user_query = state.get("user_query", "").lower()
        logger.info(f"Orchestrator analyzing query: '{user_query}'")

        step: AgentStep = {
            "agent_name": "OrchestratorAgent",
            "thought": f"Analyzed user query '{user_query}' to determine execution path.",
            "action": "Route Execution",
            "output": "Determined sub-agent sequence."
        }
        state["agent_steps"].append(step)
        return state
