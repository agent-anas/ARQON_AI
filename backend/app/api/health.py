from fastapi import APIRouter

from app.core.config import (
    PROJECT_NAME,
    PROJECT_VERSION
)

router = APIRouter()


@router.get("/health")
def health_check():

    return {
        "project": PROJECT_NAME,
        "status": "running",
        "version": PROJECT_VERSION,
        "message": "ARQON AI backend is operational"
    }