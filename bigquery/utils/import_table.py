def import_table(client, table, project_id='power-bi-m2', dataset_id='test_csv'):
    query = f"""
    SELECT *
    FROM `{project_id}.{dataset_id}.{table}`
    """

    return client.query(query).to_dataframe()

