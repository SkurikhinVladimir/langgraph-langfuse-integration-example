from pydantic_settings import BaseSettings
from pydantic import SecretStr
from typing import Optional


class Settings(BaseSettings):
    openai_api_key: SecretStr
    openai_base_url: Optional[str] = None
    openai_model: str
    mcp_url: str
    langfuse_url: Optional[str] = None
    langfuse_init_project_public_key: Optional[str] = None
    langfuse_init_project_secret_key: Optional[str] = None

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
