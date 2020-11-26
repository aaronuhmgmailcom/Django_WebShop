from django.db import models


# Create your models here.
class ProductClass(models.Model):
    class_name = models.CharField("分类名", default='', max_length=128)
    category = models.CharField("大类别", default='', max_length=128)

    def __str__(self):
        return "ProductClass class_name: %s, category: %s" % (
            self.class_name, self.category)

    class Meta:
        verbose_name = 'ProductClass'
        verbose_name_plural = 'ProductClass'