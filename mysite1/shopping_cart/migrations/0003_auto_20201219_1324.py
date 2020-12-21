# Generated by Django 2.2.12 on 2020-12-19 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0002_shoppingcart_cart_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoppingcart',
            name='purchaser_id',
        ),
        migrations.AddField(
            model_name='shoppingcart',
            name='purchaser_name',
            field=models.CharField(default='', max_length=30, null=True, verbose_name='购买者名'),
        ),
    ]