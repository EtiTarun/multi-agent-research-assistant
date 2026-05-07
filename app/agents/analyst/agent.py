from app.core.prompts import ANALYST_PROMPT

from app.core.logging_config import get_logger

from app.services.llm.mistral_service import MistralService

from app.schemas.agent_outputs import AnalysisOutput

from app.utils.json_parser import extract_json


logger = get_logger(__name__)


def analyst_agent(state):

    logger.info("Analyst Agent Started")

    state["current_agent"] = "analyst"
    state["workflow_status"] = "analyzing"

    try:

        llm_service = MistralService()

        prompt = ANALYST_PROMPT.format(
            research_findings=state["research_findings"]
        )

        response = llm_service.generate_response(
            prompt=prompt
        )

        logger.info(
            f"RAW LLM RESPONSE:\n{response}"
        )

        parsed_json = extract_json(response)

        structured_output = AnalysisOutput(
            **parsed_json
        )

        state["analysis"] = (
            structured_output.dict()
        )

        state["completed_steps"].append(
            "analyst"
        )

        logger.info(
            "Analyst Agent Completed"
        )

    except Exception as error:

        error_message = (
            f"Analyst Agent Error: {str(error)}"
        )

        logger.error(error_message)

        state["errors"].append(
            error_message
        )

        state["workflow_status"] = "failed"

        state["current_agent"] = (
            "analyst_failed"
        )

    return state