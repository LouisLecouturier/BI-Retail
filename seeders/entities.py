import random

from faker import Faker

from seeders.locations import ADDRESSES
from utils.database_connection import DatabaseConnection

NUM_SUPPLIERS = 15
NUM_CUSTOMERS = 300
NUM_ENTITIES = NUM_SUPPLIERS + NUM_CUSTOMERS

fake = Faker()


def create_entities():
    db = DatabaseConnection()

    print("Creating entities...")

    try:
        # Create base entities
        entity_values = [(i + 1,) for i in range(NUM_ENTITIES)]
        db.executemany("INSERT INTO entity (id) VALUES (%s);", entity_values)
        db.commit()

        # Prepare supplier and customer data
        supplier_data = []
        customer_data = []

        for entity_id in range(1, NUM_ENTITIES + 1):
            if entity_id <= NUM_SUPPLIERS:
                supplier_data.append(
                    (entity_id, random.randint(1, len(ADDRESSES) - 1), fake.company())
                )
            else:
                customer_data.append((entity_id, fake.first_name(), fake.last_name()))

        # Insert suppliers
        if supplier_data:
            db.executemany(
                """INSERT INTO supplier 
                (entity_id, location_id, name) 
                VALUES (%s, %s, %s);""",
                supplier_data,
            )
            db.commit()

        # Insert customers
        if customer_data:
            db.executemany(
                """INSERT INTO customer
                (entity_id, first_name, last_name)
                VALUES (%s, %s, %s);""",
                customer_data,
            )
            db.commit()

        print(f"✅ Created {NUM_ENTITIES} entities successfully")
        print(f"- {len(supplier_data)} suppliers")
        print(f"- {len(customer_data)} customers")

    except Exception as e:

        print(f"Error creating entities: {str(e)}")
        raise


if __name__ == "__main__":
    create_entities()
