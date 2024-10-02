CREATE TABLE produit (
    id INTEGER PRIMARY KEY,
    nom TEXT NOT NULL,
    prix INTEGER NOT NULL,
    quantite INTEGER NOT NULL,
    marque_id INTEGER,
    FOREIGN KEY (marque_id) REFERENCES marque(id)
);

CREATE TABLE marque (
    id INTEGER PRIMARY KEY,
    nom TEXT NOT NULL
);