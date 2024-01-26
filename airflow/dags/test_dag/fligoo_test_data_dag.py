import pandas as pd
import requests
from sqlalchemy import create_engine
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

class FlightDataETL:
    def __init__(self):
        self.api_url = 'http://api.aviationstack.com/v1/flights'
        self.api_params = {
            'access_key': 'API_KEY',
            'flight_status': 'active',
            'limit': 100
        }
        self.postgres_config = {
            "host": "postgres_db",
            "database": "testfligoo",
            "user": "fligoo",
            "password": "fligoo",
            "port": 5432 
        }

    def fetch_api_data(self):
        response = requests.get(self.api_url, params=self.api_params)
        return response.json()

    def process_data(self, raw_data):
        desired_columns = [
            'flight_date', 'flight_status', 'departure.airport', 'departure.timezone',
            'arrival.airport', 'arrival.timezone', 'arrival.terminal', 'airline.name', 'flight.number'
        ]
        normalized_df = pd.json_normalize(raw_data['data'], errors='ignore')[desired_columns]
        return normalized_df

    def save_to_postgresql(self, processed_df):
        engine = create_engine(f'postgresql+psycopg2://{self.postgres_config["user"]}:{self.postgres_config["password"]}@{self.postgres_config["host"]}:{self.postgres_config["port"]}/{self.postgres_config["database"]}')
        processed_df.to_sql("testdata", engine, if_exists="replace", index=False)
        print("Data saved to PostgreSQL")

    def run_etl(self):
        api_data = self.fetch_api_data()
        processed_data = self.process_data(api_data)
        self.save_to_postgresql(processed_data)

# Instantiate the ETL class and define the Airflow task
flight_data_etl = FlightDataETL()

flight_data_etl_dag = DAG(
    'class_based_flight_data_etl',
    schedule_interval='@daily',
    start_date=days_ago(1),
    catchup=False,
)

etl_task = PythonOperator(
    task_id='class_based_etl_flight_data',
    python_callable=flight_data_etl.run_etl,
    dag=flight_data_etl_dag,
)
