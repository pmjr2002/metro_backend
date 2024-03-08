from sqlalchemy import Column, String, ForeignKey

from database import Base


class Station(Base):
    __tablename__ = "stations"

    sid = Column(String, primary_key=True, index=True)
    name = Column(String)


class Hotspot(Base):
    __tablename__ = "hotspots"

    hid = Column(String, primary_key=True, index=True)
    name = Column(String)


class Exit(Base):
    __tablename__ = "exits"

    eid = Column(String, primary_key=True, index=True)
    name = Column(String)


class ExitHotspot(Base):
    __tablename__ = "exit_hotspots"

    eid = Column(String, ForeignKey("exits.eid"), primary_key=True)
    hid = Column(String, ForeignKey("hotspots.hid"), primary_key=True)


class ExitStation(Base):
    __tablename__ = "exit_stations"

    eid = Column(String, ForeignKey("exits.eid"), primary_key=True)
    sid = Column(String, ForeignKey("stations.sid"), primary_key=True)


class StationLine(Base):
    __tablename__ = "station_lines"

    lid = Column(String, primary_key=True, index=True)
    name = Column(String)
