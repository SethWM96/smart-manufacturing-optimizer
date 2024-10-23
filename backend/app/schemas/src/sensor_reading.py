from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class SensorReadingBase(BaseModel):
    value: float = Field(..., description="The value of the sensor reading")
    unit: str = Field(..., description="The unit of measurement (e.g., 'C', 'F', 'Pa')")
    equipment_id: int = Field(..., description="ID of the equipment from which the reading was taken")

class SensorReadingCreate(SensorReadingBase):
    pass

class SensorReadingUpdate(SensorReadingBase):
    value: Optional[float] = None
    unit: Optional[str] = None
    equipment_id: Optional[int] = None

class SensorReadingInDB(SensorReadingBase):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True

class SensorReadingResponse(SensorReadingInDB):
    pass