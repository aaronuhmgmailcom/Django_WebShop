from celery import Celery
from django.conf import settings
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite1.settings')

app=Celery('mysite1')
# ,broker='redis://@47.94.174.118:6379/1',  backend='redis://@47.94.174.118:6379/2',
app.conf.update(BROKER_URL='redis://@47.94.174.118:6379/1')
# , BACKEND='redis://@47.94.174.118:6379/2'

app.autodiscover_tasks(settings.INSTALLED_APPS)

