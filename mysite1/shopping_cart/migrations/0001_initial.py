# Generated by Django 2.2.12 on 2020-11-26 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField(default=0, verbose_name='商品ID')),
                ('purchase_quantity', models.IntegerField(default=0, verbose_name='购买数量')),
                ('purchaser_id', models.IntegerField(default=0, verbose_name='购买者ID')),
                ('status', models.IntegerField(default=0, verbose_name='购物车状态')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': 'ShoppingCart',
                'verbose_name_plural': 'ShoppingCart',
            },
        ),
    ]
