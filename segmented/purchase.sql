
CREATE TABLE purchase_order (
    id INTEGER PRIMARY KEY,
    date DATE NOT NULL,
    supplier_id INTEGER,
    FOREIGN KEY (supplier_id) REFERENCES supplier(id)
);

CREATE TABLE purchase_order_line (
    id INTEGER PRIMARY KEY,
    quantity INTEGER NOT NULL,
    unit_price INTEGER NOT NULL,
    purchase_order_id INTEGER,
    FOREIGN KEY (purchase_order_id) REFERENCES purchase_order(id),
    product_id INTEGER,
    FOREIGN KEY (product_id) REFERENCES product(id)
);

CREATE TABLE purchase_order_status (
    id INTEGER PRIMARY KEY,
    state VARCHAR(64) NOT NULL,
    date DATE NOT NULL,
    purchase_order_id INTEGER,
    FOREIGN KEY (purchase_order_id) REFERENCES purchase_order(id)
);
