from fastapi import FastAPI

from app.core.config import settings
from app.api.v1.api_router import api_router
from app.core.database import init_db


app = FastAPI(title=settings.PROJECT_NAME)

init_db()

app.include_router(api_router, prefix=settings.API_V1_STR)
 
@app.get("/")
def root():
    return {"message": "GameColec Rodando com sucesso!!"}
