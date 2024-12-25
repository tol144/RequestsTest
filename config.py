from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str

    UVICORN_HOST: str
    UVICORN_PORT: int

    @property
    def get_async_url(self):
        return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'

    @property
    def get_sync_url(self):
        return f'postgresql+psycopg2://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'

    @property
    def uvicorn_host(self):
        return self.UVICORN_HOST

    @property
    def uvicorn_port(self):
        return self.UVICORN_PORT

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
