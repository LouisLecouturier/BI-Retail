from seeders.brands import create_brands
from utils.database_connection import DatabaseConnection

print("Connecting to the database...")
db = DatabaseConnection()


print("Executing query...")

result = db.execute(open("all.sql", "r").read())
db.commit()

print(result)
create_brands()
