from fastapi import FastAPI

from app.core.config import settings
from app.api.v1.api_router import api_router
from app.core.database import init_db, SessionLocal
from app.modules.user.user_service import create_admin_if_not_exists


app = FastAPI(title=settings.PROJECT_NAME)


@app.on_event("startup")
def startup_event():
    # Cria tabelas
    init_db()

    # Cria admin padrão se não existir
    db = SessionLocal()
    try:
        create_admin_if_not_exists(
            db=db,
            email=settings.ADMIN_EMAIL,
            password=settings.ADMIN_PASSWORD
        )
    finally:
        db.close()

# Rotas da API
app.include_router(api_router, prefix=settings.API_V1_STR)


@app.get("/")
def root():
    return {"message": "GameColec rodando com sucesso 🚀"}
