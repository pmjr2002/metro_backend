from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import models
from database import get_db

router = APIRouter(tags = ["Initializers"])

@router.get("/initStations")
def initialize_stations(db: Session = Depends(get_db)):
    purpleLine = [
    "Whitefield (Kadugodi)", "Hopefarm Channasandra", "Kadugodi Tree Park", "Pattanduru Agrahara", 
    "Sri Sathya Sai Hospital", "Nallurhalli", "Kundalahalli", "Seetharamapalya", "Hoodi", 
    "Garudacharapalya", "Singayyanapalya", "Krishnarajapura (K.R.Pura)", "Benniganahalli", 
    "Baiyappanahalli", "Swami Vivekananda Road", "Indiranagara", "Halasuru", "Trinity", 
    "MG Road", "Cubbon Park", "Dr. BR. Ambedkar Station (Vidhana Soudha)", 
    "Sir M. Visveshwaraya Station (Central College)", "Nadaprabhu Kempegowda station (Majestic)", 
    "City Railway station", "Magadi Road", "Sri Balagangadharanatha Swamiji Station (Hosahalli)", 
    "Vijayanagara", "Attiguppe", "Deepanjali Nagara", "Mysuru Road", 
    "Pantharapalya (Nayandahalli)", "Rajarajeshwari Nagar", "Jnanabharathi", "Pattanagere", 
    "Kengeri Bus Terminal", "Kengeri", "Challaghatta"
]

    greenLine = [
        "Nagasandra", "Dasarahalli", "Jalahalli", "Peenya Industry", "Peenya", "Goraguntepalya", 
        "Yeshwanthpura", "Sandal Soap Factory", "Mahalakshmi", "Rajajinagara", "Kuvempu Road", 
        "Srirampura", "Sampige Road", "Nadaprabhu Kempegowda station (Majestic)", "Chikkapette", 
        "Krishna Rajendra Market", "National College", "Lalbagh Botanical Garden", "South End Circle", 
        "Jayanagara", "Rashtreeya Vidyalaya Road", "Banashankari", "Jaya Prakash Nagara", 
        "Yelachenahalli", "Konanakunte Cross", "Doddakallasandra", "Vajarahalli", "Talaghattapura", 
        "Silk Institute"
    ]

    for i, station in enumerate(purpleLine):
        newStation = models.Station(sid = f"P{i+1}", name = station)
        db.add(newStation)

    for i, station in enumerate(greenLine):
        newStation = models.Station(sid = f"G{i+1}", name = station)
        db.add(newStation)

    db.commit()    
    
    return {"message": "DB initialized"}


@router.get("/initHotspots")
def initialize_hotspots(db: Session = Depends(get_db)):
    hotspots = ["RV College", "Global Tech Park", "BDA Complex", "KIA Showroom", "Railway Station", "Bus Stop", "Cottonpete Road", "VRL Bus Stand", "Race Course", "Vidhana Soudha", "Vikas Soudha", "High Court", "Cubbon Park", "ISKCON Temple", "Orion Mall", "Shree Clinic", "Ramakrishna Home", "National College", "Sajjan Rao Circle", "Food Street"]

    for i, hotspot in enumerate(hotspots):
        newHotspot = models.Hotspot(hid = f"H{i+1}", name = hotspot)
        db.add(newHotspot)

    db.commit()

    return {"message": "DB initialized"}
