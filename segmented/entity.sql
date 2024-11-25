-- create_tables.sql

CREATE TABLE credit_note (
    id INTEGER PRIMARY KEY,
    amount INTEGER NOT NULL,
    date DATE NOT NULL,
    entity_id INTEGER,
    FOREIGN KEY (entity_id) REFERENCES entity(id)
);

CREATE TABLE dispute (
    id INTEGER PRIMARY KEY,
    amount INTEGER NOT NULL,
    date DATE NOT NULL,
    entity_id INTEGER,
    FOREIGN KEY (entity_id) REFERENCES entity(id)
);

CREATE TABLE entity (
    id INTEGER PRIMARY KEY
);
CREATE TABLE supplier (
    id INTEGER PRIMARY KEY,
    entity_id INTEGER,
    name TEXT NOT NULL,
    FOREIGN KEY (entity_id) REFERENCES entity(id)
);

CREATE TABLE customer (
    id INTEGER PRIMARY KEY,
    entity_id INTEGER,
    last_name TEXT NOT NULL,
    first_name TEXT NOT NULL,
    FOREIGN KEY (entity_id) REFERENCES entity(id)
);

CREATE TABLE employee (
    id INTEGER PRIMARY KEY,
    supervised_by INTEGER,
    last_name TEXT NOT NULL,
    first_name TEXT NOT NULL
);


