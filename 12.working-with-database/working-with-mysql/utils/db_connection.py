import mysql.connector
from config.db_config import DB_CONFIG
from utils.db_setup import create_database_if_not_exists


def get_db_connection():
    try:
        create_database_if_not_exists()

        connection = mysql.connector.connect(
            host=DB_CONFIG['host'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password'],
            database=DB_CONFIG['database']
        )
        print(f"Connected to '{DB_CONFIG.get('database')}' database on  MySQL server")
        return connection
    except mysql.connector.Error as error:
        print(f"Error connecting to MySQL: {error}")
        return None

