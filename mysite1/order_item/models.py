from django.db import models


# Create your models here.
class OrderItem(models.Model):
    order_id = models.IntegerField("订单ID", default=0)
    product_id = models.IntegerField("商品ID", default=0)
    amount = models.IntegerField("商品数量", default=0)
    price = models.DecimalField("商品单价", default=0,max_digits=10,decimal_places=2)

    def __str__(self):
        return "OrderItem order_id: %s, product_id: %s, amount: %s , price: %s" % (self.order_id, self.product_id, self.amount, self.price)

    class Meta:
        verbose_name = 'OrderItem'
        verbose_name_plural = 'OrderItem'