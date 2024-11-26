import datetime
import random

from faker import Faker

from constants import NUM_ORDERS
from seeders.entities import NUM_SUPPLIERS
from utils.database_connection import DatabaseConnection

fake = Faker()


def create_purchase_orders():
    db = DatabaseConnection()

    print("Creating purchase orders...")

    num = 0

    orders: list[dict[str, int | datetime.datetime]] = []

    for _ in range(NUM_ORDERS):

        order_date = fake.date_time()
        orders.append({"id": num + 1, "order_date": order_date})
        db.execute(
            f"""INSERT INTO purchase_order 
            (supplier_id, date) 
            VALUES 
            ('{random.randint(1, (NUM_SUPPLIERS - 1))}',
            '{order_date}'
            );"""
        )
        db.commit()
        num += 1

    print(f"✅ {num} products created.")

