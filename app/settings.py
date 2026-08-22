from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict #lets configuration values come from environment variables and .env.

#Path(__file__) = path of this file. 
# .resolve() makes it absolute. 
# .parent.parent walks up two folders (out of app/, into backend/) → BASE_DIR = the backend/ folder.
BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    app_name: str = "System Health API" #default value
    app_version: str = "1.0.0" #default value
    app_env: str #Required,no default

    database_url: str = "sqlite:///./healthapi.db" #Database connection URL.
    redis_url: str = "redis://localhost:6379/0" #Redis connection URL.

    jwt_secret_key: str #Secret key used to sign/verify JWTs.
    jwt_algorithm: str = "HS256" #signing algorithm to use for JWTs
    access_token_expire_minutes: int = 30 #JWT expires after 30 minutes.


    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


settings = Settings()