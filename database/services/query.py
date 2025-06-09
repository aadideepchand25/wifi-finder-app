from sqlalchemy.orm import Session
from fastapi import HTTPException
from ..models.wifi_id import wifi_id
from ..models.wifi_info import wifi_info
from ..models.wifi_times import wifi_times
import backend.schemas as s

def query_wifi_info_by_id(db: Session, id: int):
    wifi = db.query(wifi_id).filter(wifi_id.id == id).first()
    if not wifi:
        raise HTTPException(status_code=404, detail=f"ERROR: WiFi with that id was not found.")
    return s.read.wifi(
        location=s.create.wifi_location.model_validate(wifi),
        info=s.create.wifi_info.model_validate(wifi.info),
        times=s.create.wifi_times.model_validate(wifi.times) if wifi.times else None
    )
