from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField("用户名", max_length=64, unique=True)
    password = models.CharField("密码",default='', max_length=64)
    IMAGE = models.FileField(upload_to='myImages',default='')
    nickname= models.CharField("昵称",default='', max_length=30)
    lastname = models.CharField("名",default='', max_length=30)
    firstname = models.CharField("姓",default='', max_length=30)
    country= models.CharField("国家",default='', max_length=30)
    province= models.CharField("省份",default='', max_length=30)
    city= models.CharField("城市", default='' , max_length=30)
    gender= models.IntegerField("性别",default=0)
    age= models.IntegerField("年龄",default=0)
    birthday= models.DateField("生日",default='1900-01-01',  max_length=64)
    status= models.IntegerField("状态",default=0)
    Delivery_address1= models.CharField("收货地址1",default='', max_length=128)
    Delivery_address2= models.CharField("收货地址2",default='', max_length=128)
    EMAIL= models.EmailField("邮箱",default='', max_length=64)
    TELEPHONE= models.CharField("电话",default='', max_length=64)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    updated_time = models.DateTimeField('更新时间', auto_now=True)

    def __str__(self):
        return "User username: %s, nickname: %s, gender: %s, age: %s, status: %s" % (
            self.username, self.nickname, self.gender, self.age, self.status)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'User'
