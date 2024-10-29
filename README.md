# Smart Manufacturing Optimizer

A FastAPI-based application for managing and analyzing sensor readings in manufacturing environments. The system provides real-time monitoring, data analysis, and predictive maintenance capabilities.

## Features

- Real-time sensor data collection and storage
- RESTful API endpoints for CRUD operations
- Machine learning pipeline for anomaly detection
- React-based dashboard for data visualization
- Authentication and authorization
- Containerized deployment support

## Project Structure

```
smart-manufacturing-optimizer/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── v1/
│   │   │       ├── endpoints/
│   │   │       │   └── sensor_reading.py
│   │   │       └── router.py
│   │   ├── core/
│   │   │   └── security.py
│   │   ├── db/
│   │   │   └── src/
│   │   │       ├── base.py
│   │   │       └── session.py
│   │   ├── models/
│   │   │   └── sensor_reading.py
│   │   ├── schemas/
│   │   │   └── sensor_reading.py
│   │   └── services/
│   │       └── sensor_service.py
│   ├── tests/
│   ├── alembic/
│   └── main.py
├── frontend/
└── ml_pipeline/
```

## Prerequisites

- Python 3.9+
- PostgreSQL/SQLite
- Node.js (for frontend)
- Docker (optional)

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/smart-manufacturing-optimizer.git
cd smart-manufacturing-optimizer
```

2. Set up Python virtual environment:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows use: .\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the backend directory:
```env
DATABASE_URL=sqlite:///./sql_app.db
```

5. Initialize the database:
```bash
alembic upgrade head
```

6. Run the development server:
```bash
uvicorn app.main:app --reload
```

## API Documentation

Once the server is running, you can access:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## API Endpoints

### Sensor Readings

- `POST /api/v1/sensor-readings/`: Create a new sensor reading
- `GET /api/v1/sensor-readings/`: List all sensor readings
- `GET /api/v1/sensor-readings/{id}`: Get a specific sensor reading
- `PUT /api/v1/sensor-readings/{id}`: Update a sensor reading
- `DELETE /api/v1/sensor-readings/{id}`: Delete a sensor reading

## Running Tests

```bash
pytest
```

For verbose output:
```bash
pytest -v
```

## Development

1. Start the backend server:
```bash
uvicorn app.main:app --reload
```

2. Make API requests:
```bash
curl -X POST "http://localhost:8000/api/v1/sensor-readings/" \
     -H "Content-Type: application/json" \
     -d '{"value": 25.0, "unit": "C", "equipment_id": 1}'
```

## Docker Support

Build the Docker image:
```bash
docker build -t smart-manufacturing-optimizer .
```

Run the container:
```bash
docker run -p 8000:8000 smart-manufacturing-optimizer
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

Your Name - your.email@example.com
Project Link: https://github.com/yourusername/smart-manufacturing-optimizer