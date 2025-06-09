from create import *
from pydantic import BaseModel
from typing import Optional

##What is sent back when querying database

class wifi_id_read(wifi_location):
    id: int

class wifi(BaseModel):
    location: wifi_location
    info: wifi_info
    times: Optional[wifi_times]
    
    class Config:
        from_attributes = True