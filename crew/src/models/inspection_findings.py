from typing import Dict, Optional
from pydantic import BaseModel

class StructuralDefect(BaseModel):
    defect_type: str
    measurements: Dict[str, float]
    characteristics: Dict[str, str]
    confidence_score: float
    location: str
    severity_level: Optional[str] = None
    risk_assessment: Optional[str] = None

class InspectionContext(BaseModel):
    previous_findings: list
    property_age: int
    construction_type: str
    local_conditions: Dict[str, str]
    historical_issues: list

class InspectionReport(BaseModel):
    structural_analysis: StructuralDefect
    context_analysis: InspectionContext
    recommendations: list
    priority_level: str
    estimated_repair_timeline: str
    follow_up_actions: list