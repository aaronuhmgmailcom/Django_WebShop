from django.db import models


# Create your models here.
class PriceHistory(models.Model):
    product_id = models.IntegerField("商品ID", default=0)
    price = models.DecimalField("价格", default=0,max_digits=10,decimal_places=2)
    modify_date = models.DateTimeField("修改日期", auto_now=True)
    modify_user=models.IntegerField("Modify_user_ID", default=0)

    def __str__(self):
        return "PriceHistory product_id: %s, price: %s, modify_date: %s , modify_user: %s" % (self.product_id, self.price, self.modify_date, self.modify_user)

    class Meta:
        verbose_name = 'PriceHistory'
        verbose_name_plural = 'PriceHistory'