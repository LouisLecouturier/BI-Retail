import random

from faker import Faker

from utils.database_connection import DatabaseConnection

fake = Faker()
ADDRESSES = [(fake.street_address(), random.randint(1000, 10000)) for i in range(100)]


def create_locations():
    db = DatabaseConnection()

    print("Creating locations...")

    db.executemany(
        "INSERT INTO location (address, capacity) VALUES (%s, %s);", ADDRESSES
    )
    db.commit()

    print(f"✅ {len(ADDRESSES)} locations created.")
