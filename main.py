from seeders.brands import create_brands
from seeders.employee import create_employees
from seeders.entities import create_entities
from seeders.locations import create_locations
from seeders.products import create_products
from seeders.stores import create_stores
from seeders.warehouse import create_warehouses
from utils.database_connection import DatabaseConnection

print("Connecting to the database...")
db = DatabaseConnection()
print("Connected.")

db.clear_database()

print("Executing query...")

result = db.execute(open("all.sql", "r").read())
db.commit()

print(result)
create_brands()
create_locations()
create_entities()
create_products()
create_stores()
create_employees()
create_warehouses()
