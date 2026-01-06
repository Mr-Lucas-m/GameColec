from fastapi import APIRouter

from app.modules.auth.auth_router import router as auth_router
from app.modules.user.user_router import router as user_router
# from app.modules.console.console_router import router as console_router
# from app.modules.game.game_router import router as game_router

api_router = APIRouter()

api_router.include_router(auth_router)
api_router.include_router(user_router)
# api_router.include_router(console_router)
# api_router.include_router(game_router)
