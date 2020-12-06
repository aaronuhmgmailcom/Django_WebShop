from django.conf import settings
from mysite1.celery import app
import time
from tools.sms import YunTongXin

@app.task
def task_test():
    print('task begin...')
    time.sleep(5)
    print('task end...')

@app.task
def get_res(phone,code):
    x=YunTongXin(settings.SMS_ACCOUNT_ID,settings.SMS_ACCOUNT_TOKEN,settings.SMS_APP_ID,settings.SMS_TEMPLATE_ID)
    res= x.run(phone,code)
    return res