from django.db import models


# Create your models here.
class Order(models.Model):
    order_amount = models.DecimalField("订单金额", default=0,max_digits=10,decimal_places=2)
    create_date = models.DateTimeField('订单创建时间', auto_now_add=True)
    create_user_id = models.IntegerField("订单创建人", default=0)
    order_status = models.IntegerField("订单状态", default=0)
    receiver = models.CharField("收货人", default='', max_length=128)
    receiver_tel = models.CharField("收货人电话", default='', max_length=128)
    receiver_address = models.CharField("收货人地址", default='', max_length=128)
    pay_time = models.DateTimeField('支付时间', auto_now_add=True)
    arrive_time = models.DateTimeField('到货时间', auto_now_add=True)
    cancel_time = models.DateTimeField('取消时间', auto_now_add=True)

    def __str__(self):
        return "order date: %s, create_user: %s, order_status: %s" % (self.create_date, self.create_user_id, self.order_status)

    class Meta:
        verbose_name='order'
        verbose_name_plural='order'