from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.core.config import (
    PROJECT_NAME,
    PROJECT_FULL_NAME,
    PROJECT_VERSION,
    API_PREFIX
)

from app.core.logging_config import logger
from app.api.health import router as health_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("ARQON AI backend started successfully")

    yield

    logger.info("ARQON AI backend shutting down")


app = FastAPI(
    title=PROJECT_NAME,
    description=PROJECT_FULL_NAME,
    version=PROJECT_VERSION,
    lifespan=lifespan
)


@app.exception_handler(Exception)
async def global_exception_handler(
    request: Request,
    exc: Exception
):
    logger.exception(
        "Unhandled exception occurred: %s",
        exc
    )

    return JSONResponse(
        status_code=500,
        content={
            "status": "error",
            "message": "Internal server error"
        }
    )


@app.get("/")
def root():
    logger.info("Root endpoint accessed")

    return {
        "project": PROJECT_NAME,
        "tagline": "Intelligence Beyond Algorithms.",
        "status": "operational"
    }


app.include_router(
    health_router,
    prefix=API_PREFIX,
    tags=["System Health"]
)