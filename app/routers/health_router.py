from fastapi import APIRouter,Depends
from fastapi.responses import JSONResponse


from app.dependencies.health_dependencies import get_settings

from app.schemas.health_schema import (
    HealthResponse,
    ReadinessResponse
)

from app.services.health_service import (
    get_health_status,
    get_readiness_status
)


router = APIRouter()


@router.get(
    "/health",
    response_model=HealthResponse
)
def health(settings=Depends(get_settings)):
    return get_health_status()

@router.get(
    "/ready",
    response_model=ReadinessResponse
)
def ready(settings=Depends(get_settings)):
    result = get_readiness_status()

    if result["status"] == "not_ready":
        return JSONResponse(
            status_code=503,
            content=result
        )

    return result