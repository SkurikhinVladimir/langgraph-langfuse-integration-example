from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    graph_url: str = Field(
        ...,
    )
    graph_name: str = Field(
        ...,
    )

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
