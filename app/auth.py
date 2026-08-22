from datetime import datetime, timedelta, timezone

from jose import jwt 

from app.settings import settings

#create JWT access tokens.
def create_access_token(
    user_id: int,
    username: str,
    role: str
) -> str:

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.access_token_expire_minutes
    )

    payload = {
        "sub": str(user_id),
        "username": username,
        "role": role,
        "exp": expire
    }

    return jwt.encode(
        payload,
        settings.jwt_secret_key,
        algorithm=settings.jwt_algorithm
    )