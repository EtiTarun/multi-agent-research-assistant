from app.core.prompts import RESEARCH_PROMPT

from app.core.logging_config import get_logger

from app.services.llm.mistral_service import MistralService

from app.schemas.agent_outputs import ResearchOutput

from app.utils.json_parser import extract_json


logger = get_logger(__name__)


def researcher_agent(state):

    logger.info("Research Agent Started")

    state["current_agent"] = "researcher"
    state["workflow_status"] = "researching"

    try:

        llm_service = MistralService()

        prompt = RESEARCH_PROMPT.format(
            query=state["query"]
        )

        response = llm_service.generate_response(
            prompt=prompt
        )

        logger.info(
            f"RAW LLM RESPONSE:\n{response}"
        )

        parsed_json = extract_json(response)

        structured_output = ResearchOutput(
            **parsed_json
        )

        state["research_findings"] = (
            structured_output.dict()
        )

        state["completed_steps"].append(
            "researcher"
        )

        logger.info(
            "Research Agent Completed"
        )

    except Exception as error:

        error_message = (
            f"Research Agent Error: {str(error)}"
        )

        logger.error(error_message)

        state["errors"].append(
            error_message
        )

        state["workflow_status"] = "failed"

        state["current_agent"] = (
            "researcher_failed"
        )

    return state