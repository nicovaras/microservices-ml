from fastapi import FastAPI
from app.routers import prediction

app = FastAPI()

app.include_router(prediction.router, prefix="/predictions", tags=["Predictions"])
