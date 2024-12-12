from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseSettings):
    postgres_user: str
    postgres_password: str
    postgres_db: str

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @property
    def dns(self) -> str:
        return f"postgresql+asyncpg://{self.postgres_user}:{self.postgres_password}@db:5432/{self.postgres_db}"
    

class AppSettings(BaseSettings):
    host: str
    port: int

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
