import random

from faker import Faker
from seeders.brands import BRANDS
from utils.database_connection import DatabaseConnection

NUM_PRODUCTS = 200


fake = Faker()


def create_products():
    db = DatabaseConnection()

    print("Creating products...")

    # Create list of product tuples
    products = [
        (fake.word(), random.randint(1, 200), random.randint(1, len(BRANDS) - 1))
        for _ in range(NUM_PRODUCTS)
    ]

    # Insert all products in one operation
    db.executemany(
        "INSERT INTO product (name, price, brand_id) VALUES (%s, %s, %s);", products
    )
    db.commit()

    print(f"✅ {NUM_PRODUCTS} products created.")
