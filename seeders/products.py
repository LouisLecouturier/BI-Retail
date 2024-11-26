import random
import pandas as pd

from faker import Faker

from seeders.brands import BRANDS
from utils.database_connection import DatabaseConnection

NUM_PRODUCTS = 200


fake = Faker()

data = pd.read_csv('product_info.csv')


def create_products():
    db = DatabaseConnection()

    print("Creating products...")

    num = 0

    for i in range(NUM_PRODUCTS):
        db.execute(
            f"INSERT INTO product (name, brand_id) VALUES ('{fake.word()}', '{random.randint(1, (len(BRANDS) - 1))}');"
        )
        db.commit()
        num += 1

    print(f"✅ {num} products created.")
