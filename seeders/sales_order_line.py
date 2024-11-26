import random

from faker import Faker

from seeders.products import NUM_PRODUCTS
from seeders.sales_order import NUM_SALES
from utils.database_connection import DatabaseConnection

MIN_QUANTITY = 1
MAX_QUANTITY = 3

MIN_PRICE = 3
MAX_PRICE = 100

NUM_ORDER_LINES = NUM_SALES * 3

fake = Faker()


def create_sales_orders_lines():
    db = DatabaseConnection()

    print("Creating sales order lines...")

    # Prepare data as list of tuples
    order_lines = [
        (
            random.randint(1, (NUM_SALES - 1)),
            random.randint(1, (NUM_PRODUCTS - 1)),
            random.randint(MIN_QUANTITY, MAX_QUANTITY),
            random.randint(MIN_PRICE, MAX_PRICE),
        )
        for _ in range(NUM_ORDER_LINES)
    ]

    # Execute batch insert
    db.executemany(
        """INSERT INTO sales_order_line 
        (sales_order_id, product_id, quantity, unit_price)
        VALUES (%s, %s, %s, %s);""",
        order_lines,
    )

    db.commit()
    print(f"✅ {NUM_ORDER_LINES} sales order lines created.")
