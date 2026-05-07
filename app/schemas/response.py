from pydantic import BaseModel


class ResearchResponse(BaseModel):

    query: str

    research_findings: str

    analysis: str

    final_report: str