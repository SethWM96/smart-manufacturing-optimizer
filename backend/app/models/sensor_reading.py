from sqlalchemy import Column, Integer, Float, String, DateTime
from datetime import datetime
from app.db.src.base import Base

class SensorReading(Base):
    __tablename__ = 'sensor_readings'

    id = Column(Integer, primary_key=True, index=True)  # Primary key
    timestamp = Column(DateTime, default=datetime.utcnow)  # Time of the reading
    value = Column(Float, nullable=False)  # Value of the sensor reading
    unit = Column(String, nullable=False)  # Unit of measurement (e.g., 'C', 'F', 'Pa')
    equipment_id = Column(Integer, nullable=False)  # ID of the equipment from which the reading was taken

    def __repr__(self):
        return f"<SensorReading(id={self.id}, timestamp={self.timestamp}, value={self.value}, unit={self.unit}, equipment_id={self.equipment_id})>"