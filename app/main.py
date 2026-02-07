from fastapi import FastAPI
from .configs.database import lifespan

app = FastAPI(
    title="Habit Tracker API",
    lifespan=lifespan
)


@app.get("/")
def read_root():
    return {"Hello": "World"}
