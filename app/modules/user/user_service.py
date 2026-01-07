from sqlalchemy.orm import Session

from app.modules.user.user_model import User
from app.core.security import get_password_hash

def create_admin_if_not_exists(db: Session, email: str, password: str):
    admin = db.query(User).filter(User.email == email).first()

    if admin:
        return

    admin = User(
        email=email,
        password_hash=get_password_hash(password),
        role="admin"
    )

    db.add(admin)
    db.commit()


def create_user(db: Session, email: str, password: str, role: str):
    user = User(
        email=email,
        password_hash=get_password_hash(password),
        role=role
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()
