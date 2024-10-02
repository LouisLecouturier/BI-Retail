CREATE TABLE entrepot (
    id INTEGER PRIMARY KEY,
    nom TEXT NOT NULL
    lieu_id INTEGER,
    FOREIGN KEY (lieu_id) REFERENCES lieu(id)
);

CREATE TABLE magasin (
    id INTEGER PRIMARY KEY,
    nom TEXT NOT NULL,
    lieu_id INTEGER,
    FOREIGN KEY (lieu_id) REFERENCES lieu(id)
);

CREATE TABLE lieu (
    id INTEGER PRIMARY KEY,
    adresse TEXT NOT NULL
);