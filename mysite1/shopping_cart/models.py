from django.db import models


# Create your models here.
class ShoppingCart(models.Model):
    product_id = models.IntegerField("商品ID", default=0)
    purchase_quantity = models.IntegerField("购买数量", default=0)
    purchaser_id = models.IntegerField("购买者ID", default=0)
    status = models.IntegerField("购物车状态", default=0)
    create_date = models.DateTimeField("创建时间", auto_now_add=True)

    def __str__(self):
        return "ShoppingCart product_id: %s, purchase_quantity: %s, purchaser_id: %s, status: %s, create_date: %s" % (
            self.product_id, self.purchase_quantity,self.purchaser_id,self.status,self.create_date)

    class Meta:
        verbose_name = 'ShoppingCart'
        verbose_name_plural = 'ShoppingCart'