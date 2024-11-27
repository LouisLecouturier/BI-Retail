from utils.database_connection import DatabaseConnection

BRANDS = [
    "Hermes",
    "Chanel",
    "Dior",
    "Louis Vuitton",
    "Gucci",
    "Paco Rabanne",
    "Yves Saint Laurent",
    "Givenchy",
    "Lancome",
    "Guerlain",
    "Lacoste",
    "Kenzo",
    "Jean Paul Gaultier",
    "Hugo Boss",
]


def create_brands():
    db = DatabaseConnection()

    print("Creating brands...")

    # Convert brands to list of single-item tuples
    brand_data = [(brand,) for brand in BRANDS]

    # Execute batch insert
    db.executemany("INSERT INTO brand (name) VALUES (%s);", brand_data)
    db.commit()
    
    print(f"✅ {len(BRANDS)} brands created.")
