# tests/conftest.py
import pytest
from fastapi.testclient import TestClient
from PIL import Image
import io
from main import app
from app.crews.inspection_crew import InspectionCrew

@pytest.fixture
def test_client():
    return TestClient(app)

@pytest.fixture
def mock_image():
    """Create a simple test image"""
    img = Image.new('RGB', (100, 100), color='red')
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    return img_byte_arr.getvalue()

@pytest.fixture
def sample_room_request():
    return {
        "inspection_id": "test123",
        "room_id": "living_room",
        "photos": [
            {
                "url": "http://example.com/photo1.jpg",
                "position": "north_wall",
                "taken_at": "2024-01-16T10:00:00Z"
            }
        ],
        "previous_findings": {}
    }

@pytest.fixture
def inspection_crew():
    return InspectionCrew()