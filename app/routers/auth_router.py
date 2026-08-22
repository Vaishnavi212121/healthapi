from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth import create_access_token
from app.dependencies.auth_dependencies import get_current_user
from app.dependencies.database_dependencies import get_db
from app.models.user_model import User
from app.schemas.auth_schema import (
    ChangePasswordRequest,
    LoginRequest,
    RegisterRequest,
    TokenResponse,
    UserResponse
)
from app.security import verify_password
from app.services.auth_service import (
    authenticate_user,
    change_user_password,
    create_user
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def register(
    request: RegisterRequest,
    db: Session = Depends(get_db) #dependency injection
):
    user = create_user(
        db=db,
        username=request.username,
        password=request.password,
        role=request.role
    )

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists"
        )

    return user

@router.post(
    "/login",
    response_model=TokenResponse
)
def login(
    request: LoginRequest,
    db: Session = Depends(get_db)
):
    user = authenticate_user(
        db=db,
        username=request.username,
        password=request.password
    )

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )

    access_token = create_access_token(
        user_id=user.id,
        username=user.username,
        role=user.role
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

@router.post("/change_password")
def change_password(
    request: ChangePasswordRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if not verify_password(
        request.current_password,
        current_user.password_hash
    ):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Current password is incorrect"
        )

    change_user_password(
        current_user,
        request.new_password
    )

    db.commit()

    return {
        "message": "Password changed successfully"
    }