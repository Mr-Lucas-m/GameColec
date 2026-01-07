from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.modules.game.game_model import Game
from app.modules.console.console_model import Console


def create_game(db: Session, name: str, console_id):
    console = db.query(Console).filter(Console.id == console_id).first()
    if not console:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "success": False,
                "error": {
                    "code": "CONSOLE_NOT_FOUND",
                    "message": "Console not found"
                }
            }
        )

    game = Game(
        name=name,
        console_id=console_id
    )
    db.add(game)
    db.commit()
    db.refresh(game)
    return game


def get_all_games(db: Session):
    return db.query(Game).all()


def get_games_by_console(db: Session, console_id):
    return db.query(Game).filter(Game.console_id == console_id).all()
