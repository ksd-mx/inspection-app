import pytest
from app.crews.inspection_crew import InspectionCrew
from PIL import Image

class TestInspectionCrew:
    @pytest.mark.asyncio
    async def test_room_analysis_flow(self, mock_image):
        crew = InspectionCrew()
        photos = [Image.open(io.BytesIO(mock_image))]
        room_context = {
            "room_id": "test_room",
            "inspection_id": "test123"
        }
        
        result = await crew.analyze_room(
            photos=photos,
            room_context=room_context
        )
        
        assert "defect_analysis" in result
        assert "context_analysis" in result
        assert "report" in result

    @pytest.mark.asyncio
    async def test_crew_memory_persistence(self, mock_image):
        crew = InspectionCrew()
        photos = [Image.open(io.BytesIO(mock_image))]
        
        # Analyze first room
        result1 = await crew.analyze_room(
            photos=photos,
            room_context={"room_id": "room1"},
        )
        
        # Analyze second room
        result2 = await crew.analyze_room(
            photos=photos,
            room_context={"room_id": "room2"},
            previous_findings=result1
        )
        
        # Check if second analysis references first room's findings
        assert "previous_findings" in result2["context_analysis"]