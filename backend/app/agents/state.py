from typing import TypedDict, List, Dict, Any, Optional


class AgentStep(TypedDict):
    agent_name: str
    thought: str
    action: str
    output: Any


class AgentState(TypedDict):
    dataset_id: str
    user_query: str
    conversation_id: str
    table_name: str
    dataset_profile: Optional[Dict[str, Any]]
    cleaning_plan: Optional[List[str]]
    eda_summary: Optional[Dict[str, Any]]
    plot_specs: Optional[List[Dict[str, Any]]]
    generated_sql: Optional[str]
    sql_results: Optional[List[Dict[str, Any]]]
    ml_results: Optional[Dict[str, Any]]
    narrative_insights: Optional[List[str]]
    final_reply: Optional[str]
    agent_steps: List[AgentStep]
    error: Optional[str]
    iteration_count: int
