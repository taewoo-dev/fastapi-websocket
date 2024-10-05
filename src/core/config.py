import os
from enum import Enum
from pydantic_settings import BaseSettings, SettingsConfigDict


class ServerEnv(str, Enum):
    Local = "local"
    DEV = "dev"
    PROD = "prod"


# 현재 환경 변수에서 'ENV' 값을 읽거나 기본값으로 'local'을 사용
SERVER_ENV = os.getenv("ENV", ServerEnv.Local.value)


class Settings(BaseSettings):
    database_url: str
    database_async_url: str
    redis_host: str
    redis_port: int

    # Pydantic에서 환경 파일을 자동으로 로드
    model_config = SettingsConfigDict(env_file=f".env.{SERVER_ENV}")


settings = Settings()
