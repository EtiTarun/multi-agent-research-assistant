from langgraph.graph import StateGraph

from langgraph.graph import END


from app.graph.state import ResearchState

from app.graph.router import (
    route_after_research,
    route_after_analysis
)

from app.agents.coordinator.agent import coordinator_agent

from app.agents.researcher.agent import researcher_agent

from app.agents.analyst.agent import analyst_agent

from app.agents.writer.agent import writer_agent


def build_workflow():

    workflow = StateGraph(ResearchState)

    workflow.add_node(
        "coordinator",
        coordinator_agent
    )

    workflow.add_node(
        "researcher",
        researcher_agent
    )

    workflow.add_node(
        "analyst",
        analyst_agent
    )

    workflow.add_node(
        "writer",
        writer_agent
    )

    workflow.set_entry_point(
        "coordinator"
    )

    workflow.add_edge(
        "coordinator",
        "researcher"
    )

    workflow.add_conditional_edges(
        "researcher",
        route_after_research
    )

    workflow.add_conditional_edges(
        "analyst",
        route_after_analysis
    )

    workflow.add_edge(
        "writer",
        END
    )

    return workflow.compile()