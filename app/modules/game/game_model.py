from uuid import uuid4
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.core.database import Base


class Game(Base):
    __tablename__ = "games"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String, nullable=False)

    console_id = Column(
        UUID(as_uuid=True),
        ForeignKey("consoles.id"),
        nullable=False
    )

    console = relationship("Console")
