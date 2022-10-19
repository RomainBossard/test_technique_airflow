import os
from os.path import isfile, join
from csv import DictReader
from typing import List, Dict


AIRFLOW_HOME = os.getenv('AIRFLOW_HOME')
DATA_PATH = AIRFLOW_HOME + '/dags/data/'


def read_orders_csv() -> List[Dict]:
    files = [f for f in os.listdir(DATA_PATH) if isfile(join(DATA_PATH, f))]
    orders = []
    for file in files:
        with open(join(DATA_PATH, file)) as csvfile:
            csv = DictReader(csvfile)
            for row in csv:
                orders.append(row)
    return orders


def get_params(data: List[Dict]) -> str:
    response = "('"
    for row in data:
        response += ','.join(list(row.values()))
        response += "'),('"
    response = response[:-3]
    return response
