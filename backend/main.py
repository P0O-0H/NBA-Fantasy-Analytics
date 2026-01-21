from fastapi import FastAPI
from api.predictions_routes import router as predictions_router
from api.players_routes import router as players_router

app = FastAPI()

app.include_router(players_router, prefix="/players")
app.include_router(predictions_router, prefix="/predictions")

@app.get("/health")
def health():
    return {"status": "ok"}