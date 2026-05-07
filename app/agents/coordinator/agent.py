from app.core.logging_config import get_logger

from datetime import datetime


logger = get_logger(__name__)


def coordinator_agent(state):

    logger.info(
        f"Coordinator received query: {state['query']}"
    )

    state["current_agent"] = "coordinator"

    state["workflow_status"] = "started"

    state["metadata"] = {
        "started_at": (
            datetime.utcnow().isoformat()
        ),
        "completed_at": None
    }

    state["completed_steps"].append(
        "coordinator"
    )

    return state