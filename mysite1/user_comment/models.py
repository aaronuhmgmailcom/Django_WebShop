from django.db import models

# Create your models here.
class User_Comment(models.Model):
    user_id = models.IntegerField("用户ID" )
    product_id= models.IntegerField("商品ID")
    comment= models.CharField("评论", max_length=800)
    order_id= models.IntegerField("orderID")
    img= models.FileField(upload_to='myImages',default='')

    def __str__(self):
        return "订单评论表: 商品ID "+ str(self.product_id) + " 订单ID " + str(self.order_id)

    class Meta:
        verbose_name = 'User_Comment'
        verbose_name_plural = 'User_Comment'