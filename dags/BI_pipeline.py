from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator
from airflow.providers.operators.postgres import PostgresOperator

with DAG(
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
) as dag:
    create_psql_table_orders = PostgresOperator(
        task_id="create_psql_table_orders",
        postgres_conn_id="airflow",
        sql="""
            CREATE TABLE IF NOT EXISTS postgres.orders (
                id              INT,
                user_id         INT,
                completed_at    DATETIME,
                item_total      DECIMAL(10,2),
                shipment_total  DECIMAL(10,2)
                );
        """,
        dag=dag
    )
    read_csv = BashOperator(
        task_id='read_csv',
        bash_command=''
    )
    save_to_db = BashOperator(
        task_id='save_to_db',
        bash_command=''
    )

    create_psql_table_orders >> read_csv >> save_to_db