
from database_connection import get_connection

connection = get_connection()

cursor = connection.cursor()


cursor.execute("SELECT * FROM TABLES")