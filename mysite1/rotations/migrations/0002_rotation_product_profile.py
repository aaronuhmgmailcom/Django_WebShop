# Generated by Django 2.2.12 on 2020-12-17 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20201128_1322'),
        ('rotations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rotation',
            name='product_profile',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='product.Product'),
        ),
    ]
