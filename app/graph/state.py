from typing import TypedDict

from typing import List

from typing import Dict

from typing import Any


class ResearchState(TypedDict):

    query: str

    research_findings: Dict[str, Any]

    analysis: Dict[str, Any]

    final_report: str

    current_agent: str

    workflow_status: str

    completed_steps: List[str]

    errors: List[str]

    metadata: Dict[str, Any]