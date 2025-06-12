from sqlalchemy.orm import Session
from fastapi import HTTPException
from ..models.wifi_id import wifi_id
from geoalchemy2.shape import from_shape
from shapely.geometry import Point
import backend.schemas as s
from sqlalchemy import func

def query_wifi_info_by_id(db: Session, id: int):
    wifi = db.query(wifi_id).filter(wifi_id.id == id).first()
    if not wifi:
        raise HTTPException(status_code=404, detail=f"ERROR: WiFi with that id was not found.")
    a,b = wifi.get_lat_lon()
    return s.read.wifi(
        location=s.create.wifi_location(latitude=a,longitude=b),
        info=s.create.wifi_info.model_validate(wifi.info),
        times=s.create.wifi_times.model_validate(wifi.times) if wifi.times else None
    )

def query_wifi_id_by_location(db: Session, lat: float, long: float, radius: int):
    point = from_shape(Point(long, lat), srid=4326)
    results = (
        db.query(wifi_id)
        .filter(
            func.ST_DWithin(wifi_id.location, point, radius)
        )
        .all()
    )
    def helper(wifi):
        a,b = wifi.get_lat_lon()
        return s.read.wifi_id_read(latitude=a, longitude=b, id=wifi.id)
    return [helper(wifi) for wifi in results]