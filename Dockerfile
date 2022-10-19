FROM apache/airflow:2.4.1
COPY requirements.txt .
RUN pip install -r requirements.txt


# FROM library/postgres
# ENV POSTGRES_USER docker
# ENV POSTGRES_PASSWORD docker
# ENV POSTGRES_DB docker
# ENV
