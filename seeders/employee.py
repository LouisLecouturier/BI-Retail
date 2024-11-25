import random

from faker import Faker

from utils.database_connection import DatabaseConnection

NUM_EMPLOYEES = 20


fake = Faker()


def create_employees():
    db = DatabaseConnection()

    print("Creating employees...")

    num = 0

    for i in range(NUM_EMPLOYEES):

        supervisor = None
        if num > 8:
            supervisor = random.randint(1, 8)

        db.execute(
            f"INSERT INTO employee (name, supervised_by) VALUES ('{fake.first_name()} {fake.last_name()}', {f'{supervisor}' if supervisor else 'NULL'});"
        )
        db.commit()
        num += 1

    print(f"{num} employees created.")
