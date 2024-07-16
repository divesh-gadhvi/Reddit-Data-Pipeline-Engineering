from airflow import DAG
from datetime import datetime
import os
import sys
from airflow.operators.python_operator import PythonOperator

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

default_args = {
    'owner': 'Divesh Gadhvi',
    'start_date': datetime(2024, 7, 16)
}

file_postfix = datetime.now().strftime("%Y%m%d")

dag = DAG(
    dag_id='etl_reddit_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    tags=['reddit', 'etl', 'pipeline']
)

#Extraction from Reddit
extract = PythonOperator(
    task_id='reddit_extraction',
    pythoncallable=reddit_pipeline,
    op_kwargs={
        'file_name':f'reddit_{file_postfix}',
        'subreddit':'dataengineering',
        'time_filter':'day',
        'limit':100
    }
)

#Upload to S3