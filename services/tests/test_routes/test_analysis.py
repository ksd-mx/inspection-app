import pytest
from httpx import AsyncClient
import asyncio
from app.core.config import settings

@pytest.mark.asyncio
async def test_analyze_room_success(test_client, sample_room_request):
    async with AsyncClient(app=test_client.app, base_url="http://test") as ac:
        response = await ac.post(
            f"{settings.API_V1_STR}/analysis/room",
            json=sample_room_request
        )
    
    assert response.status_code == 200
    assert "defects" in response.json()
    assert "context_insights" in response.json()
    assert "summary" in response.json()

@pytest.mark.asyncio
async def test_analyze_room_invalid_url(test_client):
    request_data = {
        "inspection_id": "test123",
        "room_id": "living_room",
        "photos": [
            {
                "url": "not_a_valid_url",
                "position": "north_wall",
                "taken_at": "2024-01-16T10:00:00Z"
            }
        ]
    }
    
    async with AsyncClient(app=test_client.app, base_url="http://test") as ac:
        response = await ac.post(
            f"{settings.API_V1_STR}/analysis/room",
            json=request_data
        )
    
    assert response.status_code == 422  # Validation error