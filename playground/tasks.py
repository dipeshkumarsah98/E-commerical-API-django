from celery import shared_task
from time import sleep


@shared_task
def notify_customers(message):
    print('sending 10k msg...')
    sleep(10)
    print('Emails were send successfully')
