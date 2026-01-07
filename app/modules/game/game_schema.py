#app\modules\game\game_schema.py

from uuid import UUID
from pydantic import BaseModel


class GameCreate(BaseModel):
    name: str
    console_id: UUID


class GameResponse(BaseModel):
    id: UUID
    name: str
    console_id: UUID
    console_name: str
