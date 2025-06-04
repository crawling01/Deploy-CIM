import os
import mysql.connector
from dotenv import load_dotenv

# Load .env file based on environment
if os.getenv('DOCKER_DEPLOY') == 'true':
    load_dotenv('/app/.env')  # Path dalam container
else:
    load_dotenv()  # Untuk development lokal

_db_config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME'),
    'charset': 'utf8mb4'  # Tambahkan ini
}

def get_db_connection():
    """Create and return a new database connection"""
    try:
        conn = mysql.connector.connect(**_db_config)
        return conn
    except mysql.connector.Error as err:
        print(f"Error connecting to database: {err}")
        raise

class DBCursor:
    """Context manager for database cursor"""
    def __enter__(self):
        self.conn = get_db_connection()
        self.cursor = self.conn.cursor(dictionary=True)
        return self.cursor
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        if exc_type is None:
            self.conn.commit()
        else:
            self.conn.rollback()
        self.conn.close()