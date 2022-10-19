import os
import pandas as pd
from os.path import isfile, join


AIRFLOW_HOME = os.getenv('AIRFLOW_HOME')
DATA_PATH = AIRFLOW_HOME + '/dags/data/'


def read_orders_csv() -> pd.DataFrame:
    files = [f for f in os.listdir(DATA_PATH) if isfile(join(DATA_PATH, f))]
    orders = []
    for file in files:
        df = pd.read_csv(file, index_col=None, header=True)
        orders.append(df)
    orders = pd.concat(orders, axis=0, ignore_index=True)
    return orders