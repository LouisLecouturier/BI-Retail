# Big Query

## Installation

### Clé

Pour obtenir la clé de service :

1. Allez sur : [Google Cloud Console - Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts/details/104334708253224175129/keys?inv=1&invt=Abim4w&project=power-bi-m2)
2. Cliquez sur "Ajouter une clé".
3. Cliquez sur "Créer une clé".
4. Choisissez "JSON".
5. Téléchargez la clé.
6. Placez la clé dans le dossier `bigquery`.
7. Renommez le fichier de la clé en `key.json`.

### Notebook

1. Copiez le notebook `template.ipynb`.
2. Renomez le notebook copié comme vous le souhaitez (de preférence, le nom de la table que vous allez créer)
3. Le notebook contient les fonctions `import_table` et `export_table`.

### Utilisation

1. Importez les fonctions dans votre notebook :

    ```python
    from google.cloud import bigquery
    import pandas as pd
    from utils.import_table import import_table
    from utils.export import export_table

    # Initialiser le client BigQuery
    client = bigquery.Client.from_service_account_json('key.json')
    ```

2. Utilisez les fonctions `import_table` et `export_table` pour importer et exporter des tables entre PostgreSQL et BigQuery.

### Exemple

Voici un exemple d'utilisation des fonctions dans un notebook :

```python
# Initialiser le client BigQuery
client = bigquery.Client.from_service_account_json('key.json')

# Exemple d'importation d'une table
df = import_table(client, 'my_table')

# Exemple d'exportation d'une table
export_table(client, df, 'my_dataset', 'my_table')
```
