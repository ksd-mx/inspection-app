import httpx
from PIL import Image
from io import BytesIO
from typing import List

async def download_images(urls: List[str]) -> List[Image.Image]:
    """Download images from URLs"""
    images = []
    async with httpx.AsyncClient() as client:
        for url in urls:
            response = await client.get(url)
            image = Image.open(BytesIO(response.content))
            images.append(image)
    return images