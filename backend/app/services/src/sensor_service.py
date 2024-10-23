from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime

from app.models.sensor_reading import SensorReading
from app.schemas.src.sensor_reading import SensorReadingCreate, SensorReadingUpdate

class SensorService:
    @staticmethod
    async def create_sensor_reading(db: Session, sensor_reading: SensorReadingCreate) -> SensorReading:
        db_sensor_reading = SensorReading(
            value=sensor_reading.value,
            unit=sensor_reading.unit,
            equipment_id=sensor_reading.equipment_id
        )
        db.add(db_sensor_reading)
        db.commit()
        db.refresh(db_sensor_reading)
        return db_sensor_reading

    @staticmethod
    async def get_sensor_reading(db: Session, reading_id: int) -> Optional[SensorReading]:
        return db.query(SensorReading).filter(SensorReading.id == reading_id).first()

    @staticmethod
    async def get_sensor_readings(
        db: Session, 
        skip: int = 0, 
        limit: int = 100,
        equipment_id: Optional[int] = None,
        start_time: Optional[datetime] = None,
        end_time: Optional[datetime] = None
    ) -> List[SensorReading]:
        query = db.query(SensorReading)
        
        if equipment_id is not None:
            query = query.filter(SensorReading.equipment_id == equipment_id)
        if start_time is not None:
            query = query.filter(SensorReading.timestamp >= start_time)
        if end_time is not None:
            query = query.filter(SensorReading.timestamp <= end_time)
            
        return query.offset(skip).limit(limit).all()

    @staticmethod
    async def update_sensor_reading(
        db: Session, 
        reading_id: int, 
        sensor_reading: SensorReadingUpdate
    ) -> Optional[SensorReading]:
        db_sensor_reading = await SensorService.get_sensor_reading(db, reading_id)
        if db_sensor_reading:
            update_data = sensor_reading.model_dump(exclude_unset=True)
            for field, value in update_data.items():
                setattr(db_sensor_reading, field, value)
            db.commit()
            db.refresh(db_sensor_reading)
        return db_sensor_reading

    @staticmethod
    async def delete_sensor_reading(db: Session, reading_id: int) -> bool:
        db_sensor_reading = await SensorService.get_sensor_reading(db, reading_id)
        if db_sensor_reading:
            db.delete(db_sensor_reading)
            db.commit()
            return True
        return False