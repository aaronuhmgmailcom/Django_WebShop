from django.db import models


# Create your models here.
class ShoppingCart(models.Model):
    product_id = models.IntegerField("商品ID", default=0)
    purchase_quantity = models.IntegerField("购买数量", default=0)
    purchaser_name = models.CharField("购买者名", default='', max_length=30, null=True)
    status = models.IntegerField("购物车状态", default=0)
    create_date = models.DateTimeField("创建时间", auto_now_add=True)
    cart_id =models.IntegerField("cartID", default=0)

    def __str__(self):
        return "ShoppingCart product_id: %s, purchase_quantity: %s, purchaser_id: %s, status: %s, create_date: %s" % (
            self.product_id, self.purchase_quantity,self.purchaser_name,self.status,self.create_date)

    class Meta:
        verbose_name = 'ShoppingCart'
        verbose_name_plural = 'ShoppingCart'