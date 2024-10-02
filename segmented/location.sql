CREATE TABLE warehouse (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    location_id INTEGER,
    FOREIGN KEY (location_id) REFERENCES location(id)
);

CREATE TABLE store (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    location_id INTEGER,
    FOREIGN KEY (location_id) REFERENCES location(id)
);

CREATE TABLE location (
    id INTEGER PRIMARY KEY,
    adress TEXT NOT NULL
);