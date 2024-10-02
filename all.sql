-- create_TABLE IF NOT EXISTSs.sql

CREATE TABLE IF NOT EXISTS credit_note (
    id INTEGER PRIMARY KEY,
    amount INTEGER NOT NULL,
    date DATE NOT NULL,
    entity_id INTEGER,
    FOREIGN KEY (entity_id) REFERENCES entity(id)
);

CREATE TABLE IF NOT EXISTS dispute (
    id INTEGER PRIMARY KEY,
    amount INTEGER NOT NULL,
    date DATE NOT NULL,
    entity_id INTEGER,
    FOREIGN KEY (entity_id) REFERENCES entity(id)
);

CREATE TABLE IF NOT EXISTS entity (
    id INTEGER PRIMARY KEY,
    is_supplier BOOLEAN NOT NULL
);

CREATE TABLE IF NOT EXISTS supplier (
    id INTEGER PRIMARY KEY,
    entity_id INTEGER,
    name TEXT NOT NULL,
    FOREIGN KEY (entity_id) REFERENCES entity(id)
);

CREATE TABLE IF NOT EXISTS customer (
    id INTEGER PRIMARY KEY,
    entity_id INTEGER,
    last_name TEXT NOT NULL,
    first_name TEXT NOT NULL,
    FOREIGN KEY (entity_id) REFERENCES entity(id)
);

CREATE TABLE IF NOT EXISTS employee (
    id INTEGER PRIMARY KEY,
    supervised_by INTEGER,
    name TEXT NOT NULL,
    FOREIGN KEY (supervised_by) REFERENCES employee(id)
);

CREATE TABLE IF NOT EXISTS warehouse (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS store (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    location_id INTEGER,
    FOREIGN KEY (location_id) REFERENCES location(id)
);

CREATE TABLE IF NOT EXISTS location (
    id INTEGER PRIMARY KEY,
    address TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS product (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    brand_id INTEGER,
    FOREIGN KEY (brand_id) REFERENCES brand(id)
);

CREATE TABLE IF NOT EXISTS brand (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS purchase_order (
    id INTEGER PRIMARY KEY,
    date DATE NOT NULL,
    supplier_id INTEGER,
    FOREIGN KEY (supplier_id) REFERENCES supplier(id)
);

CREATE TABLE IF NOT EXISTS purchase_order_line (
    id INTEGER PRIMARY KEY,
    quantity INTEGER NOT NULL,
    unit_price INTEGER NOT NULL,
    purchase_order_id INTEGER,
    product_id INTEGER,
    FOREIGN KEY (purchase_order_id) REFERENCES purchase_order(id),
    FOREIGN KEY (product_id) REFERENCES product(id)
);

CREATE TABLE IF NOT EXISTS purchase_order_status (
    id INTEGER PRIMARY KEY,
    state VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS sales_order (
    id INTEGER PRIMARY KEY,
    date DATE NOT NULL,
    customer_id INTEGER,
    store_id INTEGER,
    FOREIGN KEY (customer_id) REFERENCES customer(id),
    FOREIGN KEY (store_id) REFERENCES store(id)
);

CREATE TABLE IF NOT EXISTS sales_order_line (
    id INTEGER PRIMARY KEY,
    quantity INTEGER NOT NULL,
    unit_price INTEGER NOT NULL,
    sales_order_id INTEGER,
    product_id INTEGER,
    FOREIGN KEY (sales_order_id) REFERENCES sales_order(id),
    FOREIGN KEY (product_id) REFERENCES product(id)
);

CREATE TABLE IF NOT EXISTS stock_movement (
    id INTEGER PRIMARY KEY,
    date DATE NOT NULL,
    product_id INTEGER,
    from_location_id INTEGER,
    to_location_id INTEGER,
    quantity INTEGER NOT NULL,
    FOREIGN KEY (product_id) REFERENCES product(id),
    FOREIGN KEY (from_location_id) REFERENCES location(id),
    FOREIGN KEY (to_location_id) REFERENCES location(id)
);

CREATE TABLE IF NOT EXISTS stock_movement_status (
    id INTEGER PRIMARY KEY,
    state VARCHAR(50) NOT NULL
);