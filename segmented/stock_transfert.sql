CREATE TABLE stock_movement (
    id INTEGER PRIMARY KEY,
    date DATE NOT NULL,
    quantity INTEGER NOT NULL,
    product_id INTEGER,
    FOREIGN KEY (product_id) REFERENCES product(id)
    from_location_id INTEGER,
    FOREIGN KEY (from_location_id) REFERENCES location(id)
    to_location_id INTEGER,
    FOREIGN KEY (to_location_id) REFERENCES location(id)
    employee_id INTEGER,
    FOREIGN KEY (employee_id) REFERENCES employee(id)
);

CREATE TABLE stock_movement_status (
    id INTEGER PRIMARY KEY,
    state VARCHAR(64) NOT NULL,
    date DATE NOT NULL,
    stock_movement_id INTEGER,
    FOREIGN KEY (stock_movement_id) REFERENCES stock_movement(id)
);