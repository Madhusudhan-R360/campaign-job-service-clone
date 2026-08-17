from pydantic_settings import (
    BaseSettings
)

from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):

    mongo_url: str

    database_name: str

    redis_host: str

    redis_port: int

    redis_db: int

    environment: str

    class Config:
        env_file = ".env"


settings = Settings()