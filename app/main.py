from fastapi import FastAPI

from app.core.config import settings
from app.core.database import Base, engine
from app.api.v1.api_router import api_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME
)

app.include_router(
    api_router,
    prefix=settings.API_V1_STR
)

 
@app.get("/")
def root():
    return {"message": "GameColec API is running"}
