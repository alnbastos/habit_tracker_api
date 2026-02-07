from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import computed_field


class Settings(BaseSettings):
    debug: bool = False

    db_user: str
    db_password: str
    db_host: str
    db_port: int = 5432
    db_name: str

    @computed_field
    @property
    def database_url(self) -> str:
        return (
            f"postgres://{self.db_user}:"
            f"{self.db_password}@"
            f"{self.db_host}:"
            f"{self.db_port}/"
            f"{self.db_name}"
        )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


settings = Settings()
