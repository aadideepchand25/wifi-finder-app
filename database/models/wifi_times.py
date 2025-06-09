from sqlalchemy import Column, Integer, Time, ForeignKey
from sqlalchemy.orm import relationship
from ..database import base

class wifi_times(base):
    __tablename__ = "wifi_times"

    id = Column(Integer, ForeignKey("wifi_id.id"), primary_key=True)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)

    wifi_id = relationship("wifi_id", back_populates="times") 