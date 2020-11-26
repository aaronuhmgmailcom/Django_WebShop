from django.db import models


# Create your models here.
class UserWallet(models.Model):
    user_id = models.IntegerField("用户ID", default=0)
    total_balance = models.DecimalField("总余额", default=0,max_digits=10, decimal_places=2)
    available_balance = models.DecimalField("可用余额", default=0,max_digits=10,decimal_places=2)
    recharge = models.DecimalField("充值金额", default=0,max_digits=10,decimal_places=2)
    consume = models.DecimalField("消费金额", default=0,max_digits=10,decimal_places=2)

    def __str__(self):
        return "UserWallet user_id: %s, total_balance: %s, available_balance: %s, recharge: %s, consume: %s" % (
            self.user_id, self.total_balance, self.available_balance, self.recharge, self.consume)

    class Meta:
        verbose_name = 'UserWallet'
        verbose_name_plural = 'UserWallet'