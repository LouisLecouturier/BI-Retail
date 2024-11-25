from faker import Faker

from utils.database_connection import DatabaseConnection

NUM_SUPPLIERS = 5
NUM_CUSTOMERS = 50
NUM_ENTITIES = NUM_SUPPLIERS + NUM_CUSTOMERS

fake = Faker()


def create_entities():
    db = DatabaseConnection()

    print("Creating entities...")

    num = 0

    entities: list[int] = []

    for i in range(NUM_ENTITIES):
        db.execute(f"INSERT INTO entity (id) VALUES ('{i + 1}');")
        db.commit()
        num += 1
        entities.append(i)

    for id in entities:

        if id < NUM_SUPPLIERS:
            db.execute(
                f"INSERT INTO supplier (entity_id, name) VALUES ('{id + 1}', '{fake.company()}')"
            )
            db.commit()
            continue

        db.execute(
            f"INSERT INTO customer (entity_id, first_name, last_name) VALUES ('{id + 1}', '{fake.first_name()}', '{fake.last_name()}')"
        )
        db.commit()
    print("Entities created.")
