import random

from django.db import models

def default_sign():
    signs = ['健身达人', '码农', '队长', '马保国', '太极拳达人']
    return random.choice(signs)

# Create your models here.
class User(models.Model):
    username = models.CharField("用户名", max_length=64, unique=True)
    password = models.CharField("密码",default='', max_length=64)
    IMAGE = models.ImageField(upload_to='myImages',null=True)
    sign = models.CharField('个人签名', max_length=50, default=default_sign)
    nickname= models.CharField("昵称",default='', max_length=30,null=True)
    lastname = models.CharField("名",default='', max_length=30,null=True)
    firstname = models.CharField("姓",default='', max_length=30,null=True)
    country= models.CharField("国家",default='', max_length=30,null=True)
    province= models.CharField("省份",default='', max_length=30,null=True)
    city= models.CharField("城市", default='' , max_length=30,null=True)
    district= models.CharField("区", default='' , max_length=30,null=True)
    gender= models.IntegerField("性别",default=0,null=True)
    age= models.IntegerField("年龄",default=0,null=True)
    birthday= models.DateField("生日",default='1900-01-01',  max_length=64,null=True)
    status= models.IntegerField("状态",default=0,null=True)
    Delivery_address1= models.CharField("收货地址1",default='', max_length=128,null=True)
    Delivery_address2= models.CharField("收货地址2",default='', max_length=128,null=True)
    EMAIL= models.EmailField("邮箱",default='', max_length=64,null=True)
    TELEPHONE= models.CharField("电话",default='', max_length=64,null=True)
    # desc= models.CharField("desc",default='', max_length=256,null=True)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    updated_time = models.DateTimeField('更新时间', auto_now=True)

    def __str__(self):
        return "User username: %s, nickname: %s, gender: %s, age: %s, status: %s" % (
            self.username, self.nickname, self.gender, self.age, self.status)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'User'
