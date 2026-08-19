import redis


REDIS_URL = "redis://localhost:6379/0"


redis_client = redis.Redis.from_url(
    REDIS_URL,
    decode_responses=True
)


def check_redis():
    try:
        redis_client.ping()

        return {
            "status": "healthy",
            "message": "Redis connection successful"
        }

    except Exception as e:
        return {
            "status": "unhealthy",
            "message": f"Redis connection failed: {str(e)}"
        }