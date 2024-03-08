from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import models, schemas
from database import get_db

router = APIRouter(prefix="/stations", tags=["stations"])


@router.get("/")
def get_stations(db: Session = Depends(get_db)):
    stations = db.query(models.Station).all()
    return {"stations": stations}


@router.get("/{sid}")
def get_station(sid: str, db: Session = Depends(get_db)):
    station = db.query(models.Station).filter(models.Station.sid == sid).first()
    if not station:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Station not found")
    return {"station": station}


@router.post("/")
def create_station(station: schemas.Station, db: Session = Depends(get_db)):
    db_station = db.query(models.Station).filter(models.Station.sid == station.sid).first()
    if db_station:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Station already exists")
    db.add(station)
    db.commit()
    db.refresh(station)
    return {"station": station}


@router.delete("/{sid}")
def delete_station(sid: int, db: Session = Depends(get_db)):
    station = db.query(models.Station).filter(models.Station.sid == sid).first()
    if not station:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Station not found")
    db.delete(station)
    db.commit()
    return {"message": "Station deleted successfully"}


@router.patch("/{sid}")
def update_station(sid: int, station: schemas.Station, db: Session = Depends(get_db)):
    db.query(models.Station).filter(models.Station.sid == sid).update(station.dict(exclude_unset=True))
    db.commit()
    return {"message": "Station updated successfully"}
