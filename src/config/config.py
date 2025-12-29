from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

BASE_DIR = Path(__file__).parent.parent.parent
ENV_DIR = BASE_DIR / ".env"


class AccessTokenSettings(BaseSettings):
    access_token_expire: int = Field(env="ACCESS_TOKEN_EXPIRE", default=60*60) 
    reset_password_token_secret: str = Field(env="RESET_PASSWORD_TOKEN_SECRET")
    verification_token_secret: str = Field(env="VERIFICATION_TOKEN_SECRET")


class Settings(BaseSettings):
    db_echo: bool = Field(env="DB_ECHO")

    postgres_user: str = Field(env="POSTGRES_USER")
    postgres_password: str = Field(env="POSTGRES_PASSWORD")
    postgres_host: str = Field(env="POSTGRES_HOST")
    postgres_port: str = Field(env="POSTGRES_PORT")
    postgres_db: str = Field(env="POSTGRES_DB")

    access_toeken_settings: AccessTokenSettings = AccessTokenSettings()

    def database_url(self) -> str:
        return f"postgresql+asyncpg://{self.postgres_user}:{self.postgres_password}@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
    
    model_config = SettingsConfigDict(
        env_file=ENV_DIR,
        env_file_encoding="utf-8", 
    )


settings = Settings()
print(settings.database_url())
