from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.dependencies import get_current_user, admin_required
from app.modules.console.console_schema import ConsoleCreate
from app.modules.console.console_service import (
    create_console,
    get_all_consoles
)

router = APIRouter(
    prefix="/consoles",
    tags=["Consoles"]
)


@router.post("")
def create(
    data: ConsoleCreate,
    db: Session = Depends(get_db),
    current_user=Depends(admin_required)
):
    console = create_console(
        db,
        data.name,
        data.company
    )

    return {
        "success": True,
        "data": console
    }


@router.get("")
def list_all(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    consoles = get_all_consoles(db)

    return {
        "success": True,
        "data": consoles
    }
