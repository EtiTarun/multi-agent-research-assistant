from fastapi import APIRouter

from app.schemas.request import ResearchRequest

from app.graph.workflow import build_workflow

from app.utils.helpers import initialize_state


router = APIRouter()

workflow = build_workflow()


@router.post("/research")
def research_topic(request: ResearchRequest):

    initial_state = initialize_state(
        query=request.query
    )

    result = workflow.invoke(
        initial_state
    )

    return result