from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    DATABASE_URL: str = Field(..., description="Database connection URL")

    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
