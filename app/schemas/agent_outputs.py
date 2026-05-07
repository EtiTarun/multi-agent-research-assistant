from pydantic import BaseModel

from typing import List


class ResearchOutput(BaseModel):

    summary: str

    key_trends: List[str]

    opportunities: List[str]

    risks: List[str]

    future_outlook: str

    sources: List[str]


class AnalysisOutput(BaseModel):

    strategic_insights: List[str]

    market_observations: List[str]

    recommendations: List[str]

    risk_assessment: List[str]