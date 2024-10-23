import unittest
from datetime import datetime
from pydantic import ValidationError
from app.schemas.src.sensor_reading import SensorReadingCreate, SensorReadingResponse

class TestSensorReadingSchemas(unittest.TestCase):

    def test_sensor_reading_create_valid(self):
        data = {
            "value": 25.6,
            "unit": "C",
            "equipment_id": 1
        }
        sensor_reading = SensorReadingCreate(**data)
        self.assertEqual(sensor_reading.value, 25.6)
        self.assertEqual(sensor_reading.unit, "C")
        self.assertEqual(sensor_reading.equipment_id, 1)

    def test_sensor_reading_create_invalid(self):
        data = {
            "value": "invalid_value",  # Invalid type
            "unit": "C",
            "equipment_id": 1
        }
        with self.assertRaises(ValidationError):
            SensorReadingCreate(**data)

    def test_sensor_reading_response_valid(self):
        data = {
            "value": 25.6,
            "unit": "C",
            "equipment_id": 1,
            "id": 101,
            "timestamp": datetime.now()
        }
        sensor_response = SensorReadingResponse(**data)
        self.assertEqual(sensor_response.id, 101)
        self.assertEqual(sensor_response.value, 25.6)

    def test_sensor_reading_response_invalid(self):
        data = {
            "value": 25.6,
            "unit": "C",
            "equipment_id": 1,
            "id": 101,
            "timestamp": "invalid_timestamp"  # Invalid timestamp
        }
        with self.assertRaises(ValidationError):
            SensorReadingResponse(**data)

if __name__ == '__main__':
    unittest.main()
