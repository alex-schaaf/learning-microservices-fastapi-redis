from pydantic import BaseSettings


class Settings(BaseSettings):
    REDIS_PUBLIC_ENDPOINT: str
    REDIS_PORT: int
    REDIS_PASSWORD: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

settings = Settings()