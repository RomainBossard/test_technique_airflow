import os
from os.path import isfile, join
from airflow.providers.postgres.hooks.postgres import PostgresHook


DATA_PATH = 'dags/data/'


def save_csv_to_db(table_name):
    pg_hook = PostgresHook(potgres_conn_id="postgres_default")
    files = [f for f in os.listdir(DATA_PATH) if isfile(join(DATA_PATH, f))]
    with pg_hook.get_conn() as connection:
        for file in files:
            pg_hook.copy_expert(f"""COPY {table_name} FROM stdin WITH CSV HEADER DELIMITER AS ','""", join(DATA_PATH, file))
            connection.commit()
