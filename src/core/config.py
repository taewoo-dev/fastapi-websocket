from enum import Enum

from pydantic_settings import BaseSettings


class Env(str, Enum):  # str과 Enum을 함께 상속받아 문자열처럼 동작하게 함
    LOCAL = "local"
    STAGE = "stage"
    PROD = "prod"


class Settings(BaseSettings):
    ENV: Env = Env.LOCAL
    DB_HOST: str = "127.0.0.1"
    DB_PORT: int = 3309
    DB_USER: str = "root"
    DB_PASSWORD: str = "qwerasd"
    DB_DB: str = "websocket-study"

    REDIS_HOST: str = "127.0.0.1"
    REDIS_PORT: int = 6380
