from datetime import datetime


def get_timestamp():

    return datetime.utcnow().isoformat()


def initialize_state(query: str):

    return {

        "query": query,

        "research_findings": {},

        "analysis": {},

        "final_report": "",

        "current_agent": "",

        "workflow_status": "running",

        "completed_steps": [],

        "errors": [],

        "metadata": {

            "started_at": get_timestamp(),

            "completed_at": None
        }
    }