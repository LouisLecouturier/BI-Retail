CREATE TABLE sales_order (
    id INTEGER PRIMARY KEY,
    date DATE NOT NULL,
    customer_id INTEGER,
    FOREIGN KEY (customer_id) REFERENCES customer(id)
    store_id INTEGER,
    FOREIGN KEY (store_id) REFERENCES store(id)
);

CREATE TABLE sales_order_line (
    id INTEGER PRIMARY KEY,
    quantity INTEGER NOT NULL,
    unit_price INTEGER NOT NULL,
    sales_order_id INTEGER,
    FOREIGN KEY (sales_order_id) REFERENCES sales_order(id)
    product_id INTEGER,
    FOREIGN KEY (product_id) REFERENCES product(id)
);