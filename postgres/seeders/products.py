import random

import pandas as pd
from faker import Faker

from seeders.brands import BRANDS
from utils.database_connection import DatabaseConnection

NUM_PRODUCTS = 200


fake = Faker()

data = pd.read_csv("product_info.csv")


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
        "INSERT INTO product (name, price, brand_id) VALUES (?, ?, ?);",
        products
    )
    db.commit()

    print(f"✅ {NUM_PRODUCTS} products created.")
