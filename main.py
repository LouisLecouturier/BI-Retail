
from seeders.brands import create_brands
from seeders.disputes_and_credits import create_disputes_and_credit
from seeders.employee import create_employees
from seeders.entities import create_entities
from seeders.locations import create_locations
from seeders.products import create_products
from seeders.purchase_order import create_purchase_orders
from seeders.purchase_order_line import create_purchase_orders_lines
from seeders.sales_order import create_sale_orders
from seeders.sales_order_line import create_sales_orders_lines
from seeders.stock_movement import create_stock_movements
from seeders.stock_movement_status import create_stock_movement_statuses
from seeders.stores import create_stores
from seeders.warehouses import create_warehouses
from utils.database_connection import DatabaseConnection

print("Connecting to the database...")
db = DatabaseConnection()
print("Connected.")

db.clear_database()

print("Executing query...")
result = db.execute(open("all.sql", "r").read())
db.commit()
print("DB schemas executed.")

print("\n=== Seeding ===\n")
create_brands()
create_locations()
create_entities()
create_products()
create_stores()
create_employees()
create_warehouses()
create_disputes_and_credit()

create_purchase_orders()
create_purchase_orders_lines()

create_sale_orders()
create_sales_orders_lines()

st_mvt = create_stock_movements()
create_stock_movement_statuses(st_mvt)

print("\n=== Seeding completed ===\n")
print("Closing connection...")
db.close_connection()
