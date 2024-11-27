CREATE TABLE product (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price INTEGER NOT NULL,
    stock INTEGER NOT NULL,
    brand_id INTEGER,
    FOREIGN KEY (brand_id) REFERENCES brand(id)
);

CREATE TABLE brand (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);