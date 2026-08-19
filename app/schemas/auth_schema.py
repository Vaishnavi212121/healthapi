from typing import Literal

from pydantic import BaseModel, Field


class RegisterRequest(BaseModel):
    username: str = Field(min_length=3)
    password: str = Field(min_length=8)
    role: Literal["ADMIN", "USER"] = "USER"


class UserResponse(BaseModel):
    id: int
    username: str
    role: str

    class Config:
        from_attributes = True

class LoginRequest(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str

class ChangePasswordRequest(BaseModel):
    current_password: str
    new_password: str = Field(min_length=8)