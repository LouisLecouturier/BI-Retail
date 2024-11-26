import datetime
import random

from faker import Faker

from constants import NUM_ORDERS
from seeders.employee import NUM_EMPLOYEES
from seeders.locations import ADDRESSES
from seeders.products import NUM_PRODUCTS
from utils.database_connection import DatabaseConnection

fake = Faker()


NUM_RANDOM_STOCK_MOVEMENT = 100


def create_stock_movements():
    db = DatabaseConnection()

    print("Creating stock movements...")

    num = 0

    stock_movements: list[dict[str, int | datetime.datetime]] = []
    movements = []

    query = """
    INSERT INTO stock_movement 
    (from_location_id, to_location_id, order_id, product_id, supervised_by, quantity, date)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    for _ in range(NUM_ORDERS):

        order_date = fake.date_time()
        stock_movements.append({"id": num + 1, "movement_date": order_date})
        movements.append(
            (
                random.randint(1, (len(ADDRESSES) - 1)),  # from_id
                random.randint(1, (len(ADDRESSES) - 1)),  # to_id
                num + 1,  # order_id
                random.randint(1, NUM_PRODUCTS),  # product_id
                random.randint(1, NUM_EMPLOYEES),  # employee_id
                random.randint(1, 100),  # quantity
                order_date,  # date
            )
        )

        num += 1

    db.executemany(query, movements)
    db.commit()
    movements = []

    for _ in range(NUM_RANDOM_STOCK_MOVEMENT):
        date = fake.date_time()
        movements.append(
            (
                random.randint(1, (len(ADDRESSES) - 1)),  # from_id
                random.randint(1, (len(ADDRESSES) - 1)),  # to_id
                None,  # order_id
                random.randint(1, NUM_PRODUCTS),  # product_id
                random.randint(1, NUM_EMPLOYEES),  # employee_id
                random.randint(-100, 100),  # quantity
                date,  # date
            )
        )

    db.executemany(query, movements)
    db.commit()

    print(f"✅ {num} stock_movements created.")
    return stock_movements
