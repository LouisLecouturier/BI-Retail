import os

from dotenv import load_dotenv
from psycopg2 import connect

load_dotenv()


class DatabaseConnection:
    def __init__(self):
        self.connection = connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
        )

    def get_connection(self):
        return self.connection

    def get_cursor(self):
        return self.connection.cursor()

    def execute(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)

    def commit(self):
        self.connection.commit()

    def close_connection(self):
        self.connection.close()
        print("Connection closed.")

    def clear_database(self):
        cursor = self.connection.cursor()
        cursor.execute(open("clear.sql", "r").read())
        self.connection.commit()
        print("Database cleared.")
