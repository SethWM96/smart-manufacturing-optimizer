from sqlalchemy import text
from app.db.src.session import engine

def test_db_connection():
    print("Attempting to connect to the database...")
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            assert result.fetchone()[0] == 1
        print("Database connection is successful!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    test_db_connection()


