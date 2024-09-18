import mysql.connector

from models.user import User
from utils.db_connection import get_db_connection

    
class UserRepository:
    def create(self, user):
        connection = get_db_connection()
        try:
            cursor = connection.cursor()
            query = "INSERT INTO users (name, email) VALUES (%s, %s)"
            cursor.execute(query, (user.name, user.email))
            connection.commit()
            print('Data inserted successfully')
            return cursor.lastrowid
        except mysql.connector.Error as e:
            print(f'Error: {e}')
        finally:
            connection.close()

    def read_all(self):
        connection = get_db_connection()
        try:
            cursor = connection.cursor()
            query = "SELECT * FROM users"
            cursor.execute(query)
            records = cursor.fetchall()
            if records:
                return records
            return None
        finally:
            connection.close()

    def read(self, user_id):
        connection = get_db_connection()
        try:
            cursor = connection.cursor()
            query = "SELECT * FROM users WHERE id = %s"
            cursor.execute(query, (user_id,))
            result = cursor.fetchone()
            if result:
                return User(*result)
            return None
        finally:
            connection.close()


    def update(self, user):
        connection = get_db_connection()
        try:
            cursor = connection.cursor()
            query = "UPDATE users SET name = %s, email = %s WHERE id = %s"
            cursor.execute(query, (user.name, user.email, user.id))
            connection.commit()
        finally:
            connection.close()


    def delete(self, user_id):
        connection = get_db_connection()
        try:
            cursor = connection.cursor()
            query = "DELETE FROM users WHERE id = %s"
            cursor.execute(query, (user_id,))
            connection.commit()
        finally:
            connection.close()