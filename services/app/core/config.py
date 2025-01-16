from pydantic.v1 import BaseSettings

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Inspector AI Analysis API"
    
    class Config:
        env_file = ".env"

settings = Settings()