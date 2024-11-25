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

    num = 0

    for i in BRANDS:
        db.execute(f"INSERT INTO brand (name) VALUES ('{i}');")
        db.commit()
        num += 1

    print(f"{num} brands created.")
