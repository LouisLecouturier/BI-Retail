from faker import Faker

from utils.database_connection import DatabaseConnection

fake = Faker()
ADDRESSES = [fake.street_address() for i in range(100)]


def create_locations():
    db = DatabaseConnection()

    print("Creating locations...")

    num = 0

    for address in ADDRESSES:
        db.execute(f"INSERT INTO location (address) VALUES ('{address}');")
        db.commit()
        num += 1

    print(f"{num} locations created.")
