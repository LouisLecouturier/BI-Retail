
import os

from utils.database_connection import DatabaseConnection


def get_all_tables():
    db = DatabaseConnection()
    cursor = db.get_cursor()
    cursor.execute("""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'public'
    """)
    tables = cursor.fetchall()
    return [table[0] for table in tables]

def export_table_to_csv(table_name, csv_file_path):
    path = os.path.join('out', csv_file_path)
    db = DatabaseConnection()
    cursor = db.get_cursor()

    query = f"COPY (SELECT * FROM {table_name}) TO STDOUT WITH CSV HEADER"
    with open(path, 'w', newline='') as csv_file:
        cursor.copy_expert(query, csv_file)

    print(f"Table {table_name} exported to {path}")

# Exporter toutes les tables
tables = get_all_tables()
for table in tables:
    export_table_to_csv(table, f"{table}.csv")for table in tables:
    export_table_to_csv(table, f"{table}.csv")