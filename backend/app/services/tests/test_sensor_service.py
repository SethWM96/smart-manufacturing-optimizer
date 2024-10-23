import unittest
import asyncio
from unittest.mock import MagicMock, Mock
from sqlalchemy.orm import Session
from app.schemas.src.sensor_reading import SensorReadingCreate, SensorReadingUpdate
from app.models.sensor_reading import SensorReading
from app.services.src.sensor_service import SensorService

class TestSensorService(unittest.TestCase):
    def setUp(self):
        self.db = MagicMock(spec=Session)
        # Create a new event loop for each test
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)

    def tearDown(self):
        self.loop.close()

    def test_create_sensor_reading(self):
        async def async_test():
            # Create test data
            sensor_data = SensorReadingCreate(value=25.0, unit="C", equipment_id=1)
            mock_sensor_reading = SensorReading(value=25.0, unit="C", equipment_id=1, id=1)
            
            # Setup mock behavior
            self.db.add = MagicMock()
            self.db.commit = MagicMock()
            self.db.refresh = MagicMock()
            
            # Mock the refresh behavior to set the id
            def mock_refresh(obj):
                obj.id = 1
            self.db.refresh.side_effect = mock_refresh

            # Call the service method
            created_reading = await SensorService.create_sensor_reading(self.db, sensor_data)
            
            # Assertions
            self.assertEqual(created_reading.value, 25.0)
            self.assertEqual(created_reading.unit, "C")
            self.assertEqual(created_reading.equipment_id, 1)
            self.db.add.assert_called_once()
            self.db.commit.assert_called_once()
            self.db.refresh.assert_called_once()

        self.loop.run_until_complete(async_test())

    def test_get_sensor_reading(self):
        async def async_test():
            # Create mock sensor reading
            mock_sensor_reading = SensorReading(value=25.0, unit="C", equipment_id=1, id=1)
            
            # Setup mock query chain
            mock_query = MagicMock()
            mock_filter = MagicMock()
            mock_first = MagicMock(return_value=mock_sensor_reading)
            
            self.db.query.return_value = mock_query
            mock_query.filter.return_value = mock_filter
            mock_filter.first.return_value = mock_sensor_reading

            # Call the service method
            fetched_reading = await SensorService.get_sensor_reading(self.db, 1)

            # Assertions
            self.assertIsNotNone(fetched_reading)
            self.assertEqual(fetched_reading.id, 1)
            self.assertEqual(fetched_reading.value, 25.0)

        self.loop.run_until_complete(async_test())

    def test_update_sensor_reading(self):
        async def async_test():
            # Create mock existing reading
            existing_reading = SensorReading(value=25.0, unit="C", equipment_id=1, id=1)
            
            # Setup mock query chain
            mock_query = MagicMock()
            mock_filter = MagicMock()
            mock_first = MagicMock(return_value=existing_reading)
            
            self.db.query.return_value = mock_query
            mock_query.filter.return_value = mock_filter
            mock_filter.first.return_value = existing_reading

            # Call the service method
            update_data = SensorReadingUpdate(value=30.0)
            updated_reading = await SensorService.update_sensor_reading(self.db, 1, update_data)

            # Assertions
            self.assertEqual(updated_reading.value, 30.0)
            self.db.commit.assert_called_once()
            self.db.refresh.assert_called_once()

        self.loop.run_until_complete(async_test())

    def test_delete_sensor_reading(self):
        async def async_test():
            # Create mock existing reading
            existing_reading = SensorReading(value=25.0, unit="C", equipment_id=1, id=1)
            
            # Setup mock query chain
            mock_query = MagicMock()
            mock_filter = MagicMock()
            mock_first = MagicMock(return_value=existing_reading)
            
            self.db.query.return_value = mock_query
            mock_query.filter.return_value = mock_filter
            mock_filter.first.return_value = existing_reading

            # Call the service method
            result = await SensorService.delete_sensor_reading(self.db, 1)

            # Assertions
            self.assertTrue(result)
            self.db.delete.assert_called_once_with(existing_reading)
            self.db.commit.assert_called_once()

        self.loop.run_until_complete(async_test())

    def test_delete_sensor_reading_not_found(self):
        async def async_test():
            # Setup mock query chain to return None
            mock_query = MagicMock()
            mock_filter = MagicMock()
            mock_first = MagicMock(return_value=None)
            
            self.db.query.return_value = mock_query
            mock_query.filter.return_value = mock_filter
            mock_filter.first.return_value = None

            # Call the service method
            result = await SensorService.delete_sensor_reading(self.db, 1)

            # Assertions
            self.assertFalse(result)
            self.db.delete.assert_not_called()
            self.db.commit.assert_not_called()

        self.loop.run_until_complete(async_test())

if __name__ == '__main__':
    unittest.main()