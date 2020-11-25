# Generated by Django 2.2.12 on 2020-11-25 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20201125_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Delivery_address1',
            field=models.CharField(default='', max_length=128, verbose_name='收货地址1'),
        ),
        migrations.AddField(
            model_name='user',
            name='Delivery_address2',
            field=models.CharField(default='', max_length=128, verbose_name='收货地址2'),
        ),
        migrations.AddField(
            model_name='user',
            name='EMAIL',
            field=models.EmailField(default='', max_length=64, verbose_name='邮箱'),
        ),
        migrations.AddField(
            model_name='user',
            name='IMAGE',
            field=models.FileField(default='', upload_to='myImages'),
        ),
        migrations.AddField(
            model_name='user',
            name='TELEPHONE',
            field=models.CharField(default='', max_length=64, verbose_name='电话'),
        ),
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.IntegerField(default=0, verbose_name='年龄'),
        ),
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateField(default='1900-01-01', max_length=64, verbose_name='生日'),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(default='', max_length=30, verbose_name='城市'),
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(default='', max_length=30, verbose_name='国家'),
        ),
        migrations.AddField(
            model_name='user',
            name='firstname',
            field=models.CharField(default='', max_length=30, verbose_name='姓'),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.IntegerField(default=0, verbose_name='性别'),
        ),
        migrations.AddField(
            model_name='user',
            name='lastname',
            field=models.CharField(default='', max_length=30, verbose_name='名'),
        ),
        migrations.AddField(
            model_name='user',
            name='nickname',
            field=models.CharField(default='', max_length=30, verbose_name='昵称'),
        ),
        migrations.AddField(
            model_name='user',
            name='province',
            field=models.CharField(default='', max_length=30, verbose_name='省份'),
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.IntegerField(default=0, verbose_name='状态'),
        ),
    ]
