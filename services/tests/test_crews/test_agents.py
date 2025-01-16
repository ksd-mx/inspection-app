import pytest
from app.crews.agents.defect_analyst import DefectAnalyst
from app.crews.agents.context_analyst import ContextAnalyst
from app.crews.agents.report_writer import ReportWriter
from PIL import Image

class TestDefectAnalyst:
    def test_agent_creation(self):
        agent = DefectAnalyst.create()
        assert agent.role == "Defect Analysis Specialist"
        assert agent.memory == True
        assert agent.verbose == True

    @pytest.mark.asyncio
    async def test_photo_analysis(self, mock_image):
        agent = DefectAnalyst.create()
        photos = [Image.open(io.BytesIO(mock_image))]
        room_context = {"room_id": "test_room"}
        
        result = await DefectAnalyst.analyze_photos(agent, photos, room_context)
        
        assert isinstance(result, dict)
        assert "defects" in result

class TestContextAnalyst:
    def test_agent_creation(self):
        agent = ContextAnalyst.create()
        assert agent.role == "Pattern Recognition Specialist"
        assert agent.memory == True
        assert agent.allow_delegation == True

    @pytest.mark.asyncio
    async def test_context_analysis(self):
        agent = ContextAnalyst.create()
        current_defects = {"defects": [{"severity": "critical"}]}
        previous_findings = {"previous_room": {"defects": []}}
        
        result = await ContextAnalyst.analyze_context(
            agent,
            current_defects,
            previous_findings
        )
        
        assert isinstance(result, dict)
        assert "patterns" in result