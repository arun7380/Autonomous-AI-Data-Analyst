from typing import Optional, List, Dict, Any
from pydantic import BaseModel


class ChatMessageRequest(BaseModel):
    dataset_id: str
    conversation_id: Optional[str] = None
    message: str


class AgentStepDetail(BaseModel):
    agent_name: str
    thought: str
    action_taken: str
    output_summary: str


class ChatMessageResponse(BaseModel):
    conversation_id: str
    reply_text: str
    agent_steps: List[AgentStepDetail]
    code_executed: Optional[str] = None
    chart_spec: Optional[Dict[str, Any]] = None
    data_table: Optional[List[Dict[str, Any]]] = None
