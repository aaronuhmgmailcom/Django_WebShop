from django.db import models


# Create your models here.
class Rotation(models.Model):
    title = models.CharField("轮播图标题", default='', max_length=64)
    img_path = models.CharField("图片地址", default='', max_length=128)
    link = models.CharField("图片链接", default='', max_length=128)
    remark = models.TextField('备注')

    def __str__(self):
        return "Rotation title: %s, img_path: %s" % (
            self.title, self.img_path)

    class Meta:
        verbose_name = 'Rotation'
        verbose_name_plural = 'Rotation'