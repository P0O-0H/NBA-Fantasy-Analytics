from fastapi import FastAPI
from api.predictions_routes import router as predictions_router

app = FastAPI()

app.include_router(predictions_router, prefix="/predictions")

@app.get("/health")
def health():
    return {"status": "ok"}