from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
import models, schemas
from database import get_db

router = APIRouter(tags=["search"])


@router.get("/search")
def search(s: str, d: str, db: Session = Depends(get_db)):
    searchS = db.query(models.Station).filter(models.Station.sid == s).first()
    searchD = db.query(models.Station).filter(models.Station.sid == d).first()

    if not searchS or not searchD:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Station not found")

    stationNames = []

    for i in range(int(s[1:]), int(d[1:]) + 1):
        station = db.query(models.Station).filter(models.Station.sid == f"S{i}").first()
            
        if station:
            stationNames.append(station.name)

    return {"stationNames": stationNames}
