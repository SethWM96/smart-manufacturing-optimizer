from fastapi import APIRouter
from app.api.v1.endpoints import sensor_reading

api_router = APIRouter()

api_router.include_router(
    sensor_reading.router,
    prefix="/sensor-readings",  
    tags=["sensor-readings"]
)