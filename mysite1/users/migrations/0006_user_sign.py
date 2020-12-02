# Generated by Django 2.2.12 on 2020-12-02 03:58

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20201201_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='sign',
            field=models.CharField(default=users.models.default_sign, max_length=50, verbose_name='个人签名'),
        ),
    ]
