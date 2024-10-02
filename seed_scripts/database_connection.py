from psycopg2 import connect
from dotenv import load_dotenv
import os

load_dotenv()


def get_connection():

    connection = connect(
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT')
    )
    
    return connection