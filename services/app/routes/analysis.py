# app/routes/analysis.py
from fastapi import APIRouter, HTTPException
from app.schemas.analysis import (
    RoomAnalysisRequest,
    RoomAnalysisResponse,
    DefectAnalysis
)
from app.core.image_utils import download_images
from app.crews.inspection_crew import InspectionCrew
from typing import List
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/room", response_model=RoomAnalysisResponse)
async def analyze_room(request: RoomAnalysisRequest):
    """
    Analyze room photos and provide comprehensive inspection results
    """
    try:
        # Download all photos for analysis
        photos = await download_images([photo.url for photo in request.photos])
        
        # Initialize inspection crew
        crew = InspectionCrew()
        
        # Prepare room context
        room_context = {
            "room_id": request.room_id,
            "inspection_id": request.inspection_id,
            "photo_positions": {
                photo.url: photo.position for photo in request.photos if photo.position
            }
        }
        
        # Run analysis
        analysis_results = await crew.analyze_room(
            photos=photos,
            room_context=room_context,
            previous_findings=request.previous_findings
        )
        
        return RoomAnalysisResponse(
            room_id=request.room_id,
            defects=analysis_results["defect_analysis"],
            context_insights=analysis_results["context_analysis"],
            summary=analysis_results["report"]
        )
        
    except Exception as e:
        logger.error(f"Error analyzing room: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Error processing room analysis: {str(e)}"
        )