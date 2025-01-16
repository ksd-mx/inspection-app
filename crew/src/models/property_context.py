from typing import List, Dict, Optional
from pydantic import BaseModel

class PropertyIssue(BaseModel):
    date: str
    type: str
    location: str
    resolved: bool
    resolution_details: Optional[str] = None

class PropertyContext(BaseModel):
    address: str
    year_built: int
    foundation_type: str
    last_inspection_date: str
    previous_issues: List[PropertyIssue]
    soil_type: str
    climate_zone: str
    building_materials: Dict[str, str]