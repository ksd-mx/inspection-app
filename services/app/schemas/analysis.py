from pydantic import BaseModel, HttpUrl
from typing import List, Optional, Dict
from datetime import datetime

class PhotoAnalysisRequest:
    url: HttpUrl
    room_id: str
    position: Optional[str]
    taken_at: datetime

class RoomAnalysisRequest(BaseModel):
    inspection_id: str
    room_id: str
    photos: List[PhotoAnalysisRequest]
    previous_findings: Optional[Dict] = {}

class DefectAnalysis(BaseModel):
    severity: str
    category: str
    description: str
    recommendations: List[str]
    location: Optional[str]

class RoomAnalysisResponse(BaseModel):
    room_id: str
    defects: List[DefectAnalysis]
    context_insights: Dict
    summary: str