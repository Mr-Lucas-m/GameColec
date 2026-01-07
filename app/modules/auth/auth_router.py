from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.dependencies import admin_required
from app.core.security import create_access_token
from app.modules.user.user_schema import UserCreate
from app.modules.user.user_service import create_user
from app.modules.auth.auth_service import authenticate_user

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register", status_code=status.HTTP_201_CREATED, dependencies=[Depends(admin_required)])
def register(user: UserCreate, db: Session = Depends(get_db)):
    try:
        created_user = create_user(
            db,
            user.email,
            user.password,
            user.role
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

    access_token = create_access_token(
        {"sub": str(created_user.id)}
    )

    return {
        "success": True,
        "data": {
            "user": {
                "id": created_user.id,
                "email": created_user.email,
                "role": created_user.role
            },
            "access_token": access_token,
            "token_type": "bearer"
        }
    }


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user, token = authenticate_user(
        db,
        form_data.username,
        form_data.password
    )

    return {
        "success": True,
        "data": {
            "user": {
                "id": user.id,
                "email": user.email,
                "role": user.role
            },
            "access_token": token,
            "token_type": "bearer"
        }
    }
