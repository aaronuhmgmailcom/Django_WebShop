from django.db import models


# Create your models here.
class SearchHistory(models.Model):
    search_words = models.CharField("查询关键字", default='', max_length=128)
    search_user = models.IntegerField("查询人", default=0)
    search_date = models.DateTimeField("查询时间", auto_now_add=True)

    def __str__(self):
        return "SearchHistory search_words: %s, search_user: %s, search_date: %s" % (
            self.search_words, self.search_user,self.search_date)

    class Meta:
        verbose_name = 'SearchHistory'
        verbose_name_plural = 'SearchHistory'