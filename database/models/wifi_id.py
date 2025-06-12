from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship
from geoalchemy2 import Geography
from geoalchemy2.shape import to_shape
from ..database import base

class wifi_id(base):
    __tablename__ = "wifi_id"
    id = Column(Integer, primary_key=True, index=True)
    location = Column(Geography(geometry_type='POINT', srid=4326), nullable=False)
    
    info = relationship("wifi_info", back_populates="wifi_id", uselist=False, cascade="all, delete-orphan")
    times = relationship("wifi_times", back_populates="wifi_id", uselist=False, cascade="all, delete-orphan")
    
    def get_lat_lon(self):
        point = to_shape(self.location)
        return (point.y, point.x)