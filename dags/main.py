
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator


from dags.etl import extraction, transformation, loading

with DAG(
    "stock_data",
    default_args={
        "depends_on_past": False,
        "email": ["brightokusi@gmail.com"],
        "email_on_failure": True,
        "email_on_retry": True,
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
        # 'end_date': datetime(2016, 1, 1),
    },
    description="A stock data web-scraping DAG",
    schedule='@daily',
    start_date=datetime(2024, 1, 7),
) as dag:
      
    begin_execution = DummyOperator(task_id='begin_execution')

    extraction = PythonOperator(task_id = 'extraction', python_callable = extraction)


    transformation = PythonOperator(task_id = 'transformation', python_callable = transformation)

    loading = PythonOperator(task_id = 'loading', python_callable = loading)



    end_execution = DummyOperator(task_id='end_execution')

    begin_execution >> extraction

    extraction >> transformation

    transformation >> loading
    
    loading >> end_execution