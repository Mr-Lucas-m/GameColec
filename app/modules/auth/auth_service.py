from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.modules.user.user_service import get_user_by_email
from app.core.security import verify_password, create_access_token


def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user or not verify_password(password, user.password_hash): # pyright: ignore[reportArgumentType]
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    token = create_access_token({"sub": str(user.id)})
    return token
