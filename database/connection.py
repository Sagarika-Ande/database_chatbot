# chatbot_project/database/connection.py
import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv() # Load environment variables from .env

def get_db_connection():
    """Establishes and returns a connection to the MySQL database."""
    try:
        connection = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            database=os.getenv("MYSQL_DATABASE")
        )
        print("Successfully connected to the database!")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

if __name__ == "__main__":
    # Example usage (for testing connection)
    conn = get_db_connection()
    if conn:
        print("Connection successful. Closing...")
        conn.close()
    else:
        print("Failed to connect.")