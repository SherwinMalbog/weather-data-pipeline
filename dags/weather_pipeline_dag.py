"""
Orchestrates the full pipeline: extract -> load -> dbt seed -> dbt run -> dbt test.

The single line at the bottom (extract >> load >> dbt_seed >> dbt_run >> dbt_test)
IS the pipeline -- everything above it just defines what each step does.
"""
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

from src.extract.fetch_weather import main as extract_main
from src.load.load_to_warehouse import main as load_main

DBT_DIR = "/opt/airflow/dbt_project"

default_args = {
    "owner": "data-eng",
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="weather_pipeline",
    description="Extract -> Load -> Transform pipeline for daily weather data",
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    tags=["data-engineering", "portfolio-project"],
) as dag:

    extract = PythonOperator(
        task_id="extract_weather_from_api",
        python_callable=extract_main,
    )

    load = PythonOperator(
        task_id="load_raw_into_warehouse",
        python_callable=load_main,
    )

    dbt_seed = BashOperator(
        task_id="dbt_seed",
        bash_command=f"cd {DBT_DIR} && dbt seed --profiles-dir {DBT_DIR}",
    )

    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command=f"cd {DBT_DIR} && dbt run --profiles-dir {DBT_DIR}",
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command=f"cd {DBT_DIR} && dbt test --profiles-dir {DBT_DIR}",
    )

    extract >> load >> dbt_seed >> dbt_run >> dbt_test
