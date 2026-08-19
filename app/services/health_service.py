import os

from dotenv import load_dotenv

from app.database import check_database
from app.redis import check_redis


load_dotenv()


APP_NAME = "System Health API"
APP_VERSION = "1.0.0"


def get_health_status():
    return {
        "status": "healthy",
        "app_name": APP_NAME,
        "version": APP_VERSION
    }


def check_environment():
    required_variables = [
        "APP_ENV"
    ]

    missing = [
        variable
        for variable in required_variables
        if not os.getenv(variable)
    ]

    if missing:
        return {
            "status": "unhealthy",
            "message": (
                f"Missing environment variables: "
                f"{', '.join(missing)}"
            )
        }

    return {
        "status": "healthy",
        "message": "Required environment variables are available"
    }


def get_readiness_status():
    environment = check_environment()
    database = check_database()
    redis = check_redis()

    checks = {
        "environment": environment,
        "database": database,
        "redis": redis
    }

    has_failure = any(
        check["status"] == "unhealthy"
        for check in checks.values()
    )

    return {
        "status": "not_ready" if has_failure else "ready",
        "app_name": APP_NAME,
        "version": APP_VERSION,
        "checks": checks
    }