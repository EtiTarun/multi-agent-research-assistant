from langgraph.graph import END


def route_after_research(state):

    if state["workflow_status"] == "failed":

        return END

    return "analyst"


def route_after_analysis(state):

    if state["workflow_status"] == "failed":

        return END

    return "writer"