import logging

import os

from logging.handlers import RotatingFileHandler

from app.core.config import settings


LOG_DIR = "logs"

os.makedirs(
    LOG_DIR,
    exist_ok=True
)


LOG_FORMAT = (
    "%(asctime)s | "
    "%(levelname)s | "
    "%(name)s | "
    "%(message)s"
)


def setup_logging():

    formatter = logging.Formatter(LOG_FORMAT)

    file_handler = RotatingFileHandler(
        filename=f"{LOG_DIR}/app.log",
        maxBytes=5 * 1024 * 1024,
        backupCount=3
    )

    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()

    console_handler.setFormatter(formatter)

    logging.basicConfig(
        level=settings.LOG_LEVEL,
        handlers=[
            file_handler,
            console_handler
        ]
    )


def get_logger(name: str):

    return logging.getLogger(name)