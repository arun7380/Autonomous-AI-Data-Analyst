from langgraph.graph import StateGraph, END
from app.agents.state import AgentState
from app.agents.orchestrator_agent import OrchestratorAgent
from app.agents.sql_agent import SQLAgent
from app.agents.reflection_agent import ReflectionAgent


def build_autonomous_analyst_graph():
    """Constructs the master LangGraph Multi-Agent State Graph for autonomous data analysis."""
    workflow = StateGraph(AgentState)

    # Add Agent Nodes
    workflow.add_node("orchestrator", OrchestratorAgent.execute)
    workflow.add_node("sql_agent", SQLAgent.execute)
    workflow.add_node("reflection", ReflectionAgent.execute)

    # Set Entry Point
    workflow.set_entry_point("orchestrator")

    # Connect Edges
    workflow.add_edge("orchestrator", "sql_agent")
    workflow.add_edge("sql_agent", "reflection")
    workflow.add_edge("reflection", END)

    return workflow.compile()


analyst_graph = build_autonomous_analyst_graph()
