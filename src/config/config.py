from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    db_url: str
    db_echo: bool


settings = Settings()