from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):

    # API:
    app_name: str = "RadarPulse"
    app_version: str = "0.1.0"
    debug: bool = False

    # Database
    database_url: str

    # Redis
    redis_url: str

    # LLM
    groq_api_key: str
    groq_model: str = "llama-3.1-8b-instant"

    # Embedding
    embedding_model: str = "all-MiniLM-L6-v2"
    embedding_dim: int = 384

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8"
    }

@lru_cache
def get_settings() -> Settings:
    return Settings()
