from pydantic import BaseModel


class Station(BaseModel):
    sid: str
    name: str


class Hotspot(BaseModel):
    hid: str
    name: str


class Exit(BaseModel):
    eid: str
    name: str


class ExitHotspot(BaseModel):
    eid: str
    hid: str


class ExitStation(BaseModel):
    eid: str
    sid: str


class StationLine(BaseModel):
    lid: str
    name: str
