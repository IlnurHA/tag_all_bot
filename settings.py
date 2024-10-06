from pydantic_settings import BaseSettings, SettingsConfigDict

from pydantic import Field
from typing import Literal

class Settings(BaseSettings):
    telegram_token: str
    api_id: str
    api_hash: str

    emoji_limit: int = Field(default=20, ge=1)

    logger_level: Literal["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"] = "INFO"

    model_config = SettingsConfigDict(
        extra="ignore",
        env_file=".env",
        env_prefix="all_tg_bot_"
    )


settings = Settings()