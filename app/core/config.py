import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    PROJECT_NAME: str = "GameColec API"

    API_V1_STR: str = os.getenv("API_V1_STR")  # type: ignore

    DATABASE_URL: str = os.getenv("DATABASE_URL")  # type: ignore

    SECRET_KEY: str = os.getenv("SECRET_KEY")  # type: ignore
    ALGORITHM: str = os.getenv("ALGORITHM")  # type: ignore
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # Admin default
    ADMIN_EMAIL: str = os.getenv("ADMIN_EMAIL")  # type: ignore
    ADMIN_PASSWORD: str = os.getenv("ADMIN_PASSWORD")  # type: ignore


settings = Settings()
