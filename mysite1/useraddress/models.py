from django.db import models

# Create your models here.
from users.models import User

class UserAddress(models.Model):
    receiver = models.CharField("收货人",default='', max_length=30,null=True)
    province = models.CharField("省",default='', max_length=64,null=True)
    city = models.CharField("市",default='', max_length=64,null=True)
    district = models.CharField("区",default='', max_length=64,null=True)
    detail_address = models.CharField("详细地址",default='', max_length=128,null=True)
    TELEPHONE = models.CharField("电话",default='', max_length=64,null=True)
    email = models.CharField("邮箱",default='', max_length=64,null=True)
    remark = models.CharField("别名(公司, 家里, 父母家)",default='', max_length=64,null=True)
    default =  models.IntegerField("状态",default=0,null=True)
    user_profile=models.ForeignKey(User, on_delete=models.CASCADE,default=None)

    def __str__(self):
        return "UserAddress receiver: %s, province: %s, city: %s, district: %s, email: %s" % (
            self.receiver, self.province, self.city, self.district, self.email)

    class Meta:
        verbose_name = 'UserAddress'
        verbose_name_plural = 'UserAddress'



