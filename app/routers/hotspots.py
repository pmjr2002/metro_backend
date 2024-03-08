from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import models, schemas
from database import get_db

router = APIRouter(prefix="/hotspots", tags=["hotspots"])

@router.get("/")
def get_hotspots(db: Session = Depends(get_db)):
    hotspots = db.query(models.Hotspot).all()
    return {"hotspots": hotspots}