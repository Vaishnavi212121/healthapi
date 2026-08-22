from sqlalchemy.orm import Session

from app.models.user_model import User
from app.security import hash_password, verify_password

def get_user_by_username(
    db: Session,
    username: str #take username
):
    return ( #Search the user table for this username and return the user if found.
        db.query(User) #Query the User table.
        .filter(User.username == username) #Only find a row where username matches.
        .first()
    )

def create_user(
    db: Session,
    username: str,
    password: str,
    role: str
):
    existing_user = get_user_by_username(
        db,
        username
    )

    if existing_user:
        return None

    user = User(
        username=username,
        password_hash=hash_password(password),
        role=role
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def authenticate_user(
    db: Session,
    username: str,
    password: str
):
    user = get_user_by_username(
        db,
        username
    )

    if not user:
        return None

    if not verify_password(
        password,
        user.password_hash
    ):
        return None

    return user

def change_user_password(
    user: User,
    new_password: str #takes the current user and new password.
):
    user.password_hash = hash_password(
        new_password #hashes the new password and replaces the old hash.
    )