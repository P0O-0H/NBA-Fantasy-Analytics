from fastapi import FastAPI
from api.predictions_routes import router as predictions_router
from api.players_routes import router as players_router
from fastapi.middleware.cors import CORSMiddleware 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(players_router, prefix="/players")
app.include_router(predictions_router, prefix="/predictions")

@app.get("/health")
def health():
    return {"status": "ok"}