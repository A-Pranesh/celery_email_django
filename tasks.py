from celery import shared_task
from time import sleep
from django.core.mail import send_mail


@shared_task
def sleepy(duration):
    sleep(10)
    send_mail('simple Mail', 'This is a sample SMTP message', 'pranesh24599@gmail.com', ['viperpranesh007@gmail.com'], )
    return None