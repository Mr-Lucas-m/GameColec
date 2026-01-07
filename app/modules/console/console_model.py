from uuid import uuid4
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

from app.core.database import Base


class Console(Base):
    __tablename__ = "consoles"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String, unique=True, nullable=False)
    company = Column(String, nullable=False)
