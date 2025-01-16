from typing import Optional, Dict, Any
from pydantic import BaseModel

class InspectionRequest(BaseModel):
    image_path: str
    property_data: Dict[str, Any]
    additional_context: Optional[Dict[str, Any]] = None

class InspectionResponse(BaseModel):
    structural_analysis: Dict[str, Any]
    context_analysis: Dict[str, Any]
    report: Dict[str, Any]
    metadata: Optional[Dict[str, Any]] = None
    additional_data: Optional[Dict[str, Any]] = None