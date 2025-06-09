from sqlalchemy import Column, Integer, Boolean, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from ..database import base

class wifi_info(base):
    __tablename__ = "wifi_info"

    id = Column(Integer, ForeignKey("wifi_id.id"), primary_key=True)
    ssid = Column(String, nullable=False)
    password = Column(String, nullable = True)
    speed = Column(Float, nullable = True)
    last_checked = Column(Date, nullable=False)
    time_restricted = Column(Boolean, nullable=False)

    wifi_id = relationship("wifi_id", back_populates="info")