import pytest
from datetime import datetime

def test_create_sensor_reading(client, db):
    test_reading = {
        "value": 25.0,
        "unit": "C",
        "equipment_id": 1
    }
    response = client.post("/api/v1/sensor-readings/", json=test_reading)
    assert response.status_code == 200
    data = response.json()
    assert data["value"] == 25.0
    assert data["unit"] == "C"
    assert data["equipment_id"] == 1
    assert "id" in data
    assert "timestamp" in data

def test_read_sensor_reading(client, db):
    # First create a reading
    test_reading = {
        "value": 25.0,
        "unit": "C",
        "equipment_id": 1
    }
    create_response = client.post("/api/v1/sensor-readings/", json=test_reading)
    assert create_response.status_code == 200
    created_data = create_response.json()
    reading_id = created_data["id"]

    # Then try to read it
    response = client.get(f"/api/v1/sensor-readings/{reading_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == reading_id
    assert data["value"] == 25.0

def test_read_sensor_reading_not_found(client, db):
    response = client.get("/api/v1/sensor-readings/999999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Sensor reading not found"

def test_read_sensor_readings(client, db):
    # Create a few readings first
    readings = [
        {"value": 25.0, "unit": "C", "equipment_id": 1},
        {"value": 26.0, "unit": "C", "equipment_id": 1},
        {"value": 27.0, "unit": "C", "equipment_id": 2}
    ]
    for reading in readings:
        response = client.post("/api/v1/sensor-readings/", json=reading)
        assert response.status_code == 200

    response = client.get("/api/v1/sensor-readings/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 3  # Should at least have our 3 readings

def test_read_sensor_readings_with_filters(client, db):
    # Create some readings with different equipment IDs
    readings = [
        {"value": 25.0, "unit": "C", "equipment_id": 1},
        {"value": 26.0, "unit": "C", "equipment_id": 1},
        {"value": 27.0, "unit": "C", "equipment_id": 2}
    ]
    for reading in readings:
        response = client.post("/api/v1/sensor-readings/", json=reading)
        assert response.status_code == 200

    # Test filtering by equipment_id
    response = client.get("/api/v1/sensor-readings/", params={
        "equipment_id": 1,
        "limit": 5,
        "skip": 0
    })
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 2  # Should only get the readings for equipment_id 1
    assert all(reading["equipment_id"] == 1 for reading in data)

def test_update_sensor_reading(client, db):
    # First create a reading
    test_reading = {
        "value": 25.0,
        "unit": "C",
        "equipment_id": 1
    }
    create_response = client.post("/api/v1/sensor-readings/", json=test_reading)
    assert create_response.status_code == 200
    created_data = create_response.json()
    reading_id = created_data["id"]

    # Then update it
    update_data = {
        "value": 30.0
    }
    response = client.put(f"/api/v1/sensor-readings/{reading_id}", json=update_data)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == reading_id
    assert data["value"] == 30.0
    assert data["unit"] == "C"  # Original value should remain
    assert data["equipment_id"] == 1  # Original value should remain

def test_update_sensor_reading_not_found(client, db):
    update_data = {
        "value": 30.0
    }
    response = client.put("/api/v1/sensor-readings/999999", json=update_data)
    assert response.status_code == 404
    assert response.json()["detail"] == "Sensor reading not found"

def test_delete_sensor_reading(client, db):
    # First create a reading
    test_reading = {
        "value": 25.0,
        "unit": "C",
        "equipment_id": 1
    }
    create_response = client.post("/api/v1/sensor-readings/", json=test_reading)
    assert create_response.status_code == 200
    created_data = create_response.json()
    reading_id = created_data["id"]

    # Then delete it
    response = client.delete(f"/api/v1/sensor-readings/{reading_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Sensor reading deleted successfully"

    # Verify it's gone
    get_response = client.get(f"/api/v1/sensor-readings/{reading_id}")
    assert get_response.status_code == 404
    assert get_response.json()["detail"] == "Sensor reading not found"

def test_delete_sensor_reading_not_found(client, db):
    response = client.delete("/api/v1/sensor-readings/999999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Sensor reading not found"