import datetime
import random

from faker import Faker

from constants import NUM_ORDERS
from seeders.entities import NUM_CUSTOMERS
from seeders.stores import NUM_STORES
from utils.database_connection import DatabaseConnection

fake = Faker()


NUM_SALES = 400


def create_sale_orders():
    db = DatabaseConnection()

    print("Creating sale orders...")

    num = 0

    sales = []
    query = """
    INSERT INTO sales_order
    (store_id, customer_id, date)
    VALUES (%s, %s, %s)
    """

    for _ in range(NUM_SALES):

        sales_date = fake.date_time()
        sales.append(
            (
                random.randint(1, (NUM_STORES - 1)),
                random.randint(1, (NUM_CUSTOMERS - 1)),
                sales_date,
            )
        )

        num += 1
    db.executemany(query, sales)
    db.commit()


    print(f"✅ {num} sales created.")
