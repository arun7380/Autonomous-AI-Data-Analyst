import os
from typing import List, Union
from pydantic import AnyHttpUrl, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "Autonomous AI Data Analyst"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    ENVIRONMENT: str = "production"
    DEBUG: bool = False

    # Security
    SECRET_KEY: str = "super_secret_development_key_change_in_production_32bytes"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days

    # Databases
    DATABASE_URL: str = "sqlite+aiosqlite:////tmp/app.db"
    DUCKDB_PATH: str = "/tmp/duckdb_store.db"

    # Redis & Celery
    REDIS_URL: str = "redis://localhost:6379/0"
    CELERY_BROKER_URL: str = "redis://localhost:6379/1"
    CELERY_RESULT_BACKEND: str = "redis://localhost:6379/2"

    # AI Model API Keys & Settings
    GOOGLE_API_KEY: str = ""
    GROQ_API_KEY: str = ""
    DEFAULT_LLM_PROVIDER: str = "google"  # options: google, groq
    DEFAULT_MODEL_NAME: str = "gemini-1.5-pro"
    FAST_MODEL_NAME: str = "gemini-1.5-flash"
    EMBEDDING_MODEL_NAME: str = "models/text-embedding-004"

    # File Storage
    UPLOAD_DIR: str = "/tmp/uploads"
    REPORTS_DIR: str = "/tmp/reports"
    MAX_FILE_SIZE_MB: int = 500

    # CORS
    BACKEND_CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://127.0.0.1:3000"]

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", case_sensitive=True, extra="ignore"
    )


settings = Settings()
