# Generated by Django 2.2.12 on 2020-12-17 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rotations', '0002_rotation_product_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='rotation',
            name='type',
            field=models.CharField(default='', max_length=128, verbose_name='分类名'),
        ),
    ]
