import datetime
import random

from faker import Faker

from utils.database_connection import DatabaseConnection

STATUS = ["pending", "processing", "shipped", "delivered", "cancelled"]


fake = Faker()


def create_stock_movement_statuses(
    stock_movements: list[dict[str, int | datetime.datetime]]
):
    db = DatabaseConnection()

    print("Creating purchase order status...")

    num = 0

    # Create list to hold all status records
    status_records = []

    for stock_movement in stock_movements:

        status_step = random.randint(1, len(STATUS))

        time_to_process = stock_movement["movement_date"] + datetime.timedelta(
            days=random.randint(1, 10)
        )
        time_to_ship = time_to_process + datetime.timedelta(days=random.randint(1, 10))
        time_to_deliver = time_to_ship + datetime.timedelta(days=random.randint(1, 10))

        status_time = [
            {"status": STATUS[0], "time": stock_movement["movement_date"]},
            {"status": STATUS[1], "time": time_to_process},
            {"status": STATUS[2], "time": time_to_ship},
            {"status": STATUS[3], "time": time_to_deliver},
        ]

        # Add each status record as a tuple
        for status in status_time[:status_step]:
            status_records.append(
                (stock_movement["id"], status["status"], status["time"])
            )
            num += 1

    # Execute single bulk insert
    db.executemany(
        """INSERT INTO stock_movement_status 
        (stock_movement_id, status, date) 
        VALUES (%s, %s, %s)""",
        status_records,
    )
    db.commit()

    print(f"✅ {num} stock movement status created.")