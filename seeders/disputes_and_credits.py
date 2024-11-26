import random

from faker import Faker

from seeders.entities import NUM_ENTITIES
from utils.database_connection import DatabaseConnection

fake = Faker()

NUM_CREDIT_NOTES = 40
NUM_DISPUTES = 20


def create_credit_notes():
    db = DatabaseConnection()

    print("Creating credit notes...")

    num = 0

    for _ in range(NUM_CREDIT_NOTES):
        db.execute(
            f"INSERT INTO credit_note (amount, date, entity_id) VALUES ('{random.randint(10, 1000)}', '{fake.date_time()}', '{random.randint(1, NUM_ENTITIES)}');"
        )
        db.commit()
        num += 1

    print(f"✅ {num} credit notes created.")


def create_disputes():
    db = DatabaseConnection()

    print("Creating credit notes...")

    num = 0

    for _ in range(NUM_DISPUTES):
        db.execute(
            f"INSERT INTO dispute (amount, date, entity_id) VALUES ('{random.randint(10, 1000)}', '{fake.date_time()}', '{random.randint(1, NUM_ENTITIES)}');"
        )
        db.commit()
        num += 1

    print(f"✅ {num} disputes created.")


def create_disputes_and_credit():
    create_credit_notes()
    create_disputes()
