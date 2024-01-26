# Data Engineer Take-Home Test - Flight Data ETL

## Quick Start Guide

### Prerequisites
- Docker
- Airflow
- Python 3.x with Pandas

### Steps to Run
1. **API Key**: Ensure you have an API key from [AviationStack](https://aviationstack.com/).

2. **Build and Run Docker**:
   - In the project directory, execute `docker-compose up` to start Airflow and PostgreSQL services.

3. **Airflow DAG Activation**:
   - Access the Airflow UI at `http://localhost:8080`. User and password is `airflow`
   - Activate the DAG named `class_based_flight_data_etl`.

4. **ETL Process**:
   - The ETL script fetches active flight data and stores it in the PostgreSQL `testfligoo` database, `testdata` table.

5. **Data Visualization with Jupyter Notebook**:
   - Access Jupyter Notebook at `http://localhost:10000`.
   - Open the provided notebook file to view and analyze the flight data in a Pandas DataFrame.