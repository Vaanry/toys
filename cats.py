#pip install python-telegram-bot==13.7

import telegram
import requests
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator


response = requests.get('https://api.thecatapi.com/v1/images/search')
cat = response.json()[0]['url']
chat_id = YOUR CHAT ID
bot = telegram.Bot(token='YOUR TOKEN')

def cats():
    bot.sendPhoto(chat_id=chat_id, photo=cat)
    
    
default_args = {
    'owner': 'vaanry',
    'depends_on_past': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2023, 8, 9),
}
schedule_interval = '0 11 * * *'


dag = DAG('cats', default_args=default_args, schedule_interval=schedule_interval)

t1 = PythonOperator(task_id='cats',
                    python_callable=cats,
                    dag=dag)

t1