import random

from faker import Faker

from constants import NUM_ORDERS
from seeders.products import NUM_PRODUCTS
from utils.database_connection import DatabaseConnection

MIN_QUANTITY = 100
MAX_QUANTITY = 1000

MIN_PRICE = 3
MAX_PRICE = 100

NUM_ORDER_LINES = NUM_ORDERS * 8

fake = Faker()


def create_purchase_orders_lines():
    db = DatabaseConnection()

    print("Creating purchase order lines...")

    # Prepare data as list of tuples
    order_lines = [
        (
            random.randint(1, (NUM_ORDERS - 1)),
            random.randint(1, (NUM_PRODUCTS - 1)),
            random.randint(MIN_QUANTITY, MAX_QUANTITY),
            random.randint(MIN_PRICE, MAX_PRICE),
        )
        for _ in range(NUM_ORDER_LINES)
    ]

    # Execute batch insert
    db.executemany(
        """INSERT INTO purchase_order_line 
        (purchase_order_id, product_id, quantity, unit_price)
        VALUES (%s, %s, %s, %s);""",
        order_lines,
    )

    db.commit()
    print(f"✅ {NUM_ORDER_LINES} purchase order lines created.")
