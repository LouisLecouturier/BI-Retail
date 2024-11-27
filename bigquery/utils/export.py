from utils.create import create_dataset
from pandas_gbq import to_gbq


def export_table(client, df, project_id, dataset_name, table_name):
    create_dataset(client, dataset_name, project_id)
    return to_gbq(
        dataframe=df,
        destination_table=f"{dataset_name}.{table_name}",
        project_id=project_id,
        if_exists="replace",  # Options : 'fail', 'replace', 'append'
    )
