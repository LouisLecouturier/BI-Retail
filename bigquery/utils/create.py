from google.cloud import bigquery

def create_dataset(client, dataset_name, project_id='power-bi-m2'):
    dataset_id = f"{project_id}.{dataset_name}"

    try:
        client.get_dataset(dataset_id)  # Vérifie si le dataset existe
        print(f"Dataset {dataset_name} déjà existant.")
    except Exception:
        # Crée un dataset si inexistant
        dataset = bigquery.Dataset(dataset_id)
        dataset.location = "US"  # Remplacez "US" par votre région si besoin
        client.create_dataset(dataset, exists_ok=True)
        print(f"Dataset {dataset_name} créé.")
