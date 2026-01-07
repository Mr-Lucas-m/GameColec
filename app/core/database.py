from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app.core.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    echo=False
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def init_db():
    """
    Inicializa o banco de dados criando todas as tabelas.
    Usado apenas em ambiente de desenvolvimento.
    """
    # IMPORTS AQUI EVITAM IMPORT CIRCULAR
    from app.modules.user.user_model import User
    from app.modules.console.console_model import Console
    from app.modules.game.game_model import Game

    Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
