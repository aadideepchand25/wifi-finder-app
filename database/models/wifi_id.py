from sqlalchemy import Column, Float, Integer
from sqlalchemy.orm import relationship
from ..database import base

class wifi_id(base):
    __tablename__ = "wifi_id"
    id = Column(Integer, primary_key=True, index=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    
    info = relationship("wifi_info", back_populates="wifi_id", uselist=False, cascade="all, delete-orphan")
    times = relationship("wifi_times", back_populates="wifi_id", uselist=False, cascade="all, delete-orphan")