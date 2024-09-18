import mysql.connector
from mysql.connector import Error
from config.db_config import DB_CONFIG



def create_database_if_not_exists():
    connection = None
    cursor = None
    try:
        # Tạo kết nối tới MySQL Server mà không chọn database
        connection = mysql.connector.connect(
            host=DB_CONFIG['host'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password']
        )

        if connection.is_connected():
            cursor = connection.cursor()

            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_CONFIG['database']}")
            print(f"Database '{DB_CONFIG['database']}' created or already exists.")

            cursor.execute(f"USE {DB_CONFIG['database']}")
            create_table_query = """
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL UNIQUE
            )
            """
            cursor.execute(create_table_query)
            print("Table 'users' created or already exists.")

    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

