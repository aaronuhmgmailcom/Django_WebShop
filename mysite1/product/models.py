from django.db import models


# Create your models here.
class Product(models.Model):
    class_ids = models.CharField("类别ID", default='', max_length=30)
    img = models.FileField(upload_to='productImages', default='')
    img2 = models.FileField(upload_to='productImages', default='')
    img3 = models.FileField(upload_to='productImages', default='')
    img4 = models.FileField(upload_to='productImages', default='')
    img5 = models.FileField(upload_to='productImages', default='')
    description = models.TextField('商品描述')
    product_name = models.CharField("商品名称", default='', max_length=128)
    price = models.DecimalField("商品价格", default=0,max_digits=10,decimal_places=2)
    discount = models.DecimalField("折扣", default=0,max_digits=10,decimal_places=2)
    amount = models.DecimalField("库存数量", default=0,max_digits=10,decimal_places=2)
    productor = models.CharField("生产商", default='', max_length=128)
    author = models.CharField("生产者", default='', max_length=128)
    status = models.IntegerField("状态", default=0)

    def __str__(self):
        return "Product class_ids: %s, product_name: %s, price: %s , discount: %s,amount: %s,productor: %s,author: %s,status: %s" % (
        self.class_ids, self.product_name, self.price, self.discount,self.amount, self.productor, self.author, self.status)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Product'