# Generated by Django 2.2.12 on 2020-11-26 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField(default=0, verbose_name='订单ID')),
                ('product_id', models.IntegerField(default=0, verbose_name='商品ID')),
                ('amount', models.IntegerField(default=0, verbose_name='商品数量')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='商品单价')),
            ],
            options={
                'verbose_name': 'order',
                'verbose_name_plural': 'order',
            },
        ),
    ]
