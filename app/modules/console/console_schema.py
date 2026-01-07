#app\modules\console\console_schema.py

from uuid import UUID
from pydantic import BaseModel


class ConsoleCreate(BaseModel):
    name: str
    company: str


class ConsoleResponse(BaseModel):
    id: UUID
    name: str
    company: str

    class Config:
        from_attributes = True
