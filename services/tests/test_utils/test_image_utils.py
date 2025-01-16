import pytest
from app.core.image_utils import download_images
from unittest.mock import patch

@pytest.mark.asyncio
async def test_download_images_success():
    test_urls = ["http://example.com/test.jpg"]
    
    with patch('httpx.AsyncClient.get') as mock_get:
        mock_get.return_value.content = open('tests/fixtures/test_image.png', 'rb').read()
        images = await download_images(test_urls)
        
        assert len(images) == 1
        assert isinstance(images[0], Image.Image)

@pytest.mark.asyncio
async def test_download_images_failure():
    test_urls = ["http://invalid-url.com/test.jpg"]
    
    with pytest.raises(Exception):
        await download_images(test_urls)