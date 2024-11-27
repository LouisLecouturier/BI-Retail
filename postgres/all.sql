-- create_TABLE IF NOT EXISTSs.sql
CREATE TABLE IF NOT EXISTS entity (
    id SERIAL PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS location (
    id SERIAL PRIMARY KEY,
    capacity INTEGER NOT NULL,
    address TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS credit_note (
    id SERIAL PRIMARY KEY,
    amount INTEGER NOT NULL,
    date DATE NOT NULL,
    entity_id INTEGER,
    FOREIGN KEY (entity_id) REFERENCES entity(id)
);

CREATE TABLE IF NOT EXISTS dispute (
    id SERIAL PRIMARY KEY,
    amount INTEGER NOT NULL,
    date DATE NOT NULL,
    entity_id INTEGER,
    FOREIGN KEY (entity_id) REFERENCES entity(id)
);

CREATE TABLE IF NOT EXISTS supplier (
    id SERIAL PRIMARY KEY,
    entity_id INTEGER,
    location_id INTEGER,
    name TEXT NOT NULL,
    FOREIGN KEY (entity_id) REFERENCES entity(id),
    FOREIGN KEY (location_id) REFERENCES location(id)
);

CREATE TABLE IF NOT EXISTS customer (
    id SERIAL PRIMARY KEY,
    entity_id INTEGER,
    last_name TEXT NOT NULL,
    first_name TEXT NOT NULL,
    FOREIGN KEY (entity_id) REFERENCES entity(id)
);

CREATE TABLE IF NOT EXISTS employee (
    id SERIAL PRIMARY KEY,
    supervised_by INTEGER,
    name TEXT NOT NULL,
    FOREIGN KEY (supervised_by) REFERENCES employee(id)
);


CREATE TABLE IF NOT EXISTS warehouse (
    id SERIAL PRIMARY KEY,
    location_id INTEGER,
    name TEXT NOT NULL,
    FOREIGN KEY (location_id) REFERENCES location(id)
);

CREATE TABLE IF NOT EXISTS store (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    location_id INTEGER,
    FOREIGN KEY (location_id) REFERENCES location(id)
);

CREATE TABLE IF NOT EXISTS brand (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS product (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    price INTEGER NOT NULL,
    brand_id INTEGER,
    FOREIGN KEY (brand_id) REFERENCES brand(id)
);

CREATE TABLE IF NOT EXISTS purchase_order (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    supplier_id INTEGER,
    FOREIGN KEY (supplier_id) REFERENCES supplier(id)
);

CREATE TABLE IF NOT EXISTS purchase_order_line (
    id SERIAL PRIMARY KEY,
    quantity INTEGER NOT NULL,
    unit_price INTEGER NOT NULL,
    purchase_order_id INTEGER,
    product_id INTEGER,
    FOREIGN KEY (purchase_order_id) REFERENCES purchase_order(id),
    FOREIGN KEY (product_id) REFERENCES product(id)
);


CREATE TABLE IF NOT EXISTS sales_order (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    customer_id INTEGER,
    store_id INTEGER,
    FOREIGN KEY (customer_id) REFERENCES customer(id),
    FOREIGN KEY (store_id) REFERENCES store(id)
);

CREATE TABLE IF NOT EXISTS sales_order_line (
    id SERIAL PRIMARY KEY,
    quantity INTEGER NOT NULL,
    unit_price INTEGER NOT NULL,
    sales_order_id INTEGER,
    product_id INTEGER,
    FOREIGN KEY (sales_order_id) REFERENCES sales_order(id),
    FOREIGN KEY (product_id) REFERENCES product(id)
);

CREATE TABLE IF NOT EXISTS stock_movement (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    product_id INTEGER,
    from_location_id INTEGER,
    to_location_id INTEGER,
    order_id INTEGER,
    employee_id INTEGER,
    quantity INTEGER NOT NULL,
    FOREIGN KEY (product_id) REFERENCES product(id),
    FOREIGN KEY (from_location_id) REFERENCES location(id),
    FOREIGN KEY (to_location_id) REFERENCES location(id),
    FOREIGN KEY (order_id) REFERENCES purchase_order(id),
    FOREIGN KEY (employee_id) REFERENCES employee(id)
);

CREATE TABLE IF NOT EXISTS stock_movement_status (
    id SERIAL PRIMARY KEY,
    stock_movement_id INTEGER,
    status VARCHAR(50) NOT NULL,
    date DATE,
    FOREIGN KEY (stock_movement_id) REFERENCES stock_movement(id)
);