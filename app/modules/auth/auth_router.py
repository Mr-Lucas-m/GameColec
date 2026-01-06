from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.modules.user.user_schema import UserCreate
from app.modules.user.user_service import create_user
from app.modules.auth.auth_service import authenticate_user

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    created_user = create_user(
        db,
        user.email,
        user.password,
        user.role
    )

    return {
        "success": True,
        "data": created_user
    }


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    token = authenticate_user(
        db,
        form_data.username,
        form_data.password
    )

    return {
        "success": True,
        "data": {
            "access_token": token,
            "token_type": "bearer"
        }
    }
