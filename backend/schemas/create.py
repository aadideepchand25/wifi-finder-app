from pydantic import BaseModel
from typing import Optional
from datetime import date, time

##what is sent when querying database

class wifi_id(BaseModel):
    id: int

class wifi_location(BaseModel):
    latitude: float
    longitude: float
    
    class Config:
        from_attributes = True
    
class wifi_info(BaseModel):
    ssid: str
    password: Optional[str] = None
    speed: Optional[float] = None
    last_checked: date
    time_restricted: bool = False
        
    class Config:
        from_attributes = True
    
class wifi_times(BaseModel):
    start_time: time
    end_time: time
        
    class Config:
        from_attributes = True