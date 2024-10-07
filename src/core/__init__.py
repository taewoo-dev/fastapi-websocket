from core.config import Settings


def get_settings() -> Settings:
    return Settings(_env_file=".env.local", _env_file_encoding="utf-8")  # type: ignore


settings = get_settings()
