-- create_tables.sql

CREATE TABLE avoir (
    id INTEGER PRIMARY KEY,
    montant INTEGER NOT NULL,
    date DATE NOT NULL,
    entite_id INTEGER,
    FOREIGN KEY (entite_id) REFERENCES entite(id)
);

CREATE TABLE litige (
    id INTEGER PRIMARY KEY,
    montant INTEGER NOT NULL,
    date DATE NOT NULL,
    fournisseur_id INTEGER,
    FOREIGN KEY (fournisseur_id) REFERENCES fournisseur(id)
);

CREATE TABLE entite (
    id INTEGER PRIMARY KEY,
);

CREATE TABLE fournisseur (
    id INTEGER PRIMARY KEY,
    entite_id INTEGER,
    nom TEXT NOT NULL,
    FOREIGN KEY (entite_id) REFERENCES entite(id)
);

CREATE TABLE client (
    id INTEGER PRIMARY KEY,
    entite_id INTEGER,
    nom TEXT NOT NULL,
    prenom TEXT NOT NULL,
    FOREIGN KEY (entite_id) REFERENCES entite(id)
);


