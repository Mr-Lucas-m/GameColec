from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.modules.console.console_model import Console


def create_console(db: Session, name: str, company: str):
    exists = db.query(Console).filter(Console.name == name).first()
    if exists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "success": False,
                "error": {
                    "code": "CONSOLE_EXISTS",
                    "message": "Console with this name already exists"
                }
            }
        )

    console = Console(
        name=name,
        company=company
    )
    db.add(console)
    db.commit()
    db.refresh(console)
    return console


def get_all_consoles(db: Session):
    return db.query(Console).all()


def get_console_by_id(db: Session, console_id):
    return db.query(Console).filter(Console.id == console_id).first()
