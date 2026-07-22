import uuid
from fastapi import APIRouter
from app.schemas.chat import ChatMessageRequest, ChatMessageResponse, AgentStepDetail
from app.graphs.main_graph import analyst_graph

router = APIRouter(prefix="/chat", tags=["Multi-Agent Chat"])


@router.post("", response_model=ChatMessageResponse)
async def chat_with_dataset(payload: ChatMessageRequest):
    """Executes multi-agent LangGraph workflow in response to user natural language query."""
    conv_id = payload.conversation_id or str(uuid.uuid4())

    initial_state = {
        "dataset_id": payload.dataset_id,
        "user_query": payload.message,
        "conversation_id": conv_id,
        "table_name": payload.dataset_id,
        "dataset_profile": None,
        "cleaning_plan": None,
        "eda_summary": None,
        "plot_specs": None,
        "generated_sql": None,
        "sql_results": None,
        "ml_results": None,
        "narrative_insights": None,
        "final_reply": None,
        "agent_steps": [],
        "error": None,
        "iteration_count": 0
    }

    final_state = analyst_graph.invoke(initial_state)

    steps = [
        AgentStepDetail(
            agent_name=step["agent_name"],
            thought=step["thought"],
            action_taken=step["action"],
            output_summary=str(step["output"])
        )
        for step in final_state.get("agent_steps", [])
    ]

    sql = final_state.get("generated_sql")
    rows = final_state.get("sql_results")

    reply_text = f"Analyzed query '{payload.message}'. Executed DuckDB SQL: `{sql}`."

    return ChatMessageResponse(
        conversation_id=conv_id,
        reply_text=reply_text,
        agent_steps=steps,
        code_executed=sql,
        data_table=rows
    )
