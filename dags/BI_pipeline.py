from airflow import DAG
from datetime import datetime, timedelta
from airflow.utils.trigger_rule import TriggerRule
from airflow.providers.operators.postgres import PostgresOperator
from airflow.operators.python import PythonOperator
from dags.tasks.csv import read_orders_csv, get_params


dag = DAG(
    'BI_pipeline',
    default_args={
        'depends_on_past': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=5),
    },
    description='a basic BI pipeline',
    schedule=timedelta(1),
    start_date=datetime(2022, 10, 15),
    catchup=False,
    tags=['bi_pipeline'],
)

create_psql_table_orders = PostgresOperator(
    task_id="create_psql_table_orders",
    postgres_conn_id="postgres_default",
    sql="""
        CREATE TABLE IF NOT EXISTS orders (
            id              INT,
            user_id         INT,
            completed_at    DATETIME,
            item_total      DECIMAL(10,2),
            shipment_total  DECIMAL(10,2)
            );
    """,
    dag=dag
)

load_csv = PythonOperator(
    task_id="load_csv",
    python_callable=read_orders_csv,
    dag=dag
)

params = PythonOperator(
    task_id="get_params",
    python_callable=get_params,
    params=load_csv,
    dag=dag
)

save_to_db = PostgresOperator(
    task_id="save_to_db",
    postgres_conn_id="postgres_localhost",
    sql="""
        INSERT INTO orders
        VALUES %s
    """,
    params=params,
    dag=dag
)

create_psql_table_orders >> load_csv >> params >> save_to_db
