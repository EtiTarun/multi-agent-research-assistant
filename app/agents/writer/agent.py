from datetime import datetime

from app.core.prompts import WRITER_PROMPT
from app.core.logging_config import get_logger
from app.services.llm.mistral_service import MistralService


logger = get_logger(__name__)


def writer_agent(state):

    logger.info("Writer Agent Started")

    state["current_agent"] = "writer"

    try:

        llm_service = MistralService()

        prompt = WRITER_PROMPT.format(
            research_findings=state["research_findings"],
            analysis=state["analysis"]
        )

        response = llm_service.generate_response(
            prompt=prompt
        )

        state["final_report"] = response

        # Avoid duplicate writer entries
        if "writer" not in state["completed_steps"]:

            state["completed_steps"].append(
                "writer"
            )

        state["workflow_status"] = "completed"

        state["current_agent"] = "completed"

        state["metadata"]["completed_at"] = (
            datetime.utcnow().isoformat()
        )

        logger.info(
            "Writer Agent Completed"
        )

    except Exception as error:

        error_message = (
            f"Writer Agent Error: {str(error)}"
        )

        logger.error(error_message)

        state["errors"].append(
            error_message
        )

        state["workflow_status"] = "failed"

        state["current_agent"] = (
            "writer_failed"
        )

    return state