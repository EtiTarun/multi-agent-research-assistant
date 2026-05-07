from fastapi import FastAPI

from app.core.config import settings

from app.core.logging_config import setup_logging

from app.api.routes import router


setup_logging()


app = FastAPI(
    title=settings.PROJECT_NAME
)


app.include_router(router)


@app.get("/")
def root():

    return {
        "message": "Multi-Agent Research Assistant API is running."
    }