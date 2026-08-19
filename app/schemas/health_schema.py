from typing import Dict

from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str
    app_name: str
    version: str


class CheckResponse(BaseModel):
    status: str
    message: str


class ReadinessResponse(BaseModel):
    status: str
    app_name: str
    version: str
    checks: Dict[str, CheckResponse]