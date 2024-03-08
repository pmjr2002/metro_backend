from fastapi import FastAPI
from routers import stations, initDB, hotspots
from database import engine
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(stations.router)
app.include_router(hotspots.router)
app.include_router(initDB.router)