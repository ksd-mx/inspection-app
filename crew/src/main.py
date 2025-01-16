import os
from pathlib import Path
from dotenv import load_dotenv
from fastapi import FastAPI
from api.router import router

# Load environment variables
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# Create FastAPI app
app = FastAPI(
    title="Inspection AI Service",
    description="AI-powered structural inspection analysis service",
    version="1.0.0"
)

# Add router
app.include_router(router, prefix="/api/v1")

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)