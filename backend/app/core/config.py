import os
from dotenv import load_dotenv

load_dotenv()

from typing import Optional

class Settings:
    PROJECT_NAME: str = "Todo App Phase II"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = os.getenv("SECRET_KEY", "changethis_secret_key_extremely_insecure_for_dev")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    DATABASE_URL: Optional[str] = os.getenv("DATABASE_URL")

    raw_origins = os.getenv("BACKEND_CORS_ORIGINS")
    if raw_origins:
        BACKEND_CORS_ORIGINS: list = [origin.strip() for origin in raw_origins.split(",")]
    else:
    raw_origins = os.getenv("BACKEND_CORS_ORIGINS")
    if raw_origins:
        BACKEND_CORS_ORIGINS: list = [origin.strip() for origin in raw_origins.split(",")]
    else:
        # Allow all origins for Hackathon/Vercel deployment flexibility
        BACKEND_CORS_ORIGINS: list = ["*"]

settings = Settings()
