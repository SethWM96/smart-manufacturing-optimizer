from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime

from app.db.src.session import get_db
from app.schemas.src.sensor_reading import (
    SensorReadingCreate,
    SensorReadingResponse,
    SensorReadingUpdate
)
from app.services.src.sensor_service import SensorService

router = APIRouter()

@router.post("/", response_model=SensorReadingResponse)
async def create_sensor_reading(
    sensor_reading: SensorReadingCreate,
    db: Session = Depends(get_db)
):
    return await SensorService.create_sensor_reading(db, sensor_reading)

@router.get("/{reading_id}", response_model=SensorReadingResponse)
async def read_sensor_reading(reading_id: int, db: Session = Depends(get_db)):
    db_sensor_reading = await SensorService.get_sensor_reading(db, reading_id)
    if db_sensor_reading is None:
        raise HTTPException(status_code=404, detail="Sensor reading not found")
    return db_sensor_reading

@router.get("/", response_model=List[SensorReadingResponse])
async def read_sensor_readings(
    skip: int = 0,
    limit: int = 100,
    equipment_id: Optional[int] = None,
    start_time: Optional[datetime] = None,
    end_time: Optional[datetime] = None,
    db: Session = Depends(get_db)
):
    sensor_readings = await SensorService.get_sensor_readings(
        db, skip=skip, limit=limit, 
        equipment_id=equipment_id,
        start_time=start_time,
        end_time=end_time
    )
    return sensor_readings

@router.put("/{reading_id}", response_model=SensorReadingResponse)
async def update_sensor_reading(
    reading_id: int,
    sensor_reading: SensorReadingUpdate,
    db: Session = Depends(get_db)
):
    db_sensor_reading = await SensorService.update_sensor_reading(db, reading_id, sensor_reading)
    if db_sensor_reading is None:
        raise HTTPException(status_code=404, detail="Sensor reading not found")
    return db_sensor_reading

@router.delete("/{reading_id}")
async def delete_sensor_reading(reading_id: int, db: Session = Depends(get_db)):
    success = await SensorService.delete_sensor_reading(db, reading_id)
    if not success:
        raise HTTPException(status_code=404, detail="Sensor reading not found")
    return {"message": "Sensor reading deleted successfully"}
