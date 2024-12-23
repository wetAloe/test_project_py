from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseSettings):
    postgres_user: str
    postgres_password: str
    postgres_db: str
    postgres_host: str
    postgres_port: int

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @property
    def dns(self) -> str:
        return f"postgresql+asyncpg://{self.postgres_user}:{self.postgres_password}@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
    

class RuntimeSettings(BaseSettings):
    host: str
    port: int

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
