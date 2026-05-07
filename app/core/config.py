from dotenv import load_dotenv

import os


load_dotenv()


class Settings:

    PROJECT_NAME: str = os.getenv(
        "PROJECT_NAME",
        "Multi-Agent Research Assistant"
    )

    APP_ENV: str = os.getenv(
        "APP_ENV",
        "development"
    )

    LOG_LEVEL: str = os.getenv(
        "LOG_LEVEL",
        "INFO"
    )

    MISTRAL_API_KEY: str = os.getenv(
        "MISTRAL_API_KEY"
    )

    MISTRAL_MODEL: str = os.getenv(
        "MISTRAL_MODEL",
        "mistral-small-latest"
    )


settings = Settings()