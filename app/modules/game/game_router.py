from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.dependencies import get_current_user, admin_required
from app.modules.game.game_schema import GameCreate
from app.modules.game.game_service import (
    create_game,
    get_all_games,
    get_games_by_console
)
from app.modules.console.console_service import get_console_by_id

router = APIRouter(
    prefix="/games",
    tags=["Games"]
)


@router.post("")
def create(
    data: GameCreate,
    db: Session = Depends(get_db),
    current_user=Depends(admin_required)
):
    game = create_game(
        db,
        data.name,
        data.console_id
    )

    return {
        "success": True,
        "data": {
            "id": game.id,
            "name": game.name,
            "console_id": game.console_id,
            "console_name": game.console.name
        }
    }


@router.get("")
def list_all(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    games = get_all_games(db)

    return {
        "success": True,
        "data": [
            {
                "id": game.id,
                "name": game.name,
                "console_id": game.console_id,
                "console_name": game.console.name
            }
            for game in games
        ]
    }


@router.get("/consoles/{console_id}")
def list_by_console(
    console_id,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    games = get_games_by_console(db, console_id)

    return {
        "success": True,
        "data": [
            {
                "id": game.id,
                "name": game.name,
                "console_id": game.console_id,
                "console_name": game.console.name
            }
            for game in games
        ]
    }
