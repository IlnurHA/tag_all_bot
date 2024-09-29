from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    telegram_token: str

    model_config = SettingsConfigDict(
        extra="ignore",
        env_file=".env",
        env_prefix="all_tg_bot_"
    )


settings = Settings()