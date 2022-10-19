from airflow import DAG
from datetime import datetime, timedelta
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.operators.python import PythonOperator
from tasks.csv import save_csv_to_db


dag = DAG(
    'BI_pipeline',
    description='a basic BI pipeline',
    schedule_interval=None,
    start_date=datetime(2022, 10, 15),
)

create_psql_table_orders = PostgresOperator(
    task_id="create_psql_table_orders",
    postgres_conn_id="postgres_default",
    sql="""
        CREATE TABLE IF NOT EXISTS orders (
            id              INT,
            user_id         INT,
            completed_at    DATE,
            item_total      DECIMAL(10,2),
            shipment_total  DECIMAL(10,2)
            );
    """,
    dag=dag
)

save_orders_to_db = PythonOperator(
    task_id="save_orders_to_db",
    python_callable=save_csv_to_db,
    op_kwargs={'table_name': 'orders'},
    dag=dag
)

create_psql_table_orders >> save_orders_to_db
