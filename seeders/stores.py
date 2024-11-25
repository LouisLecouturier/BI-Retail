import random

from faker import Faker

from seeders.locations import ADDRESSES
from utils.database_connection import DatabaseConnection

NUM_STORES = 10


fake = Faker()


def create_stores():
    db = DatabaseConnection()

    print("Creating stores...")

    num = 0

    for i in range(NUM_STORES):
        db.execute(
            f"INSERT INTO store (name, location_id) VALUES ('{fake.street_address()}', '{random.randint(1, (len(ADDRESSES) - 1))}');"
        )
        db.commit()
        num += 1

    print(f"{num} stores created.")
