# Generated by Django 2.2.12 on 2020-12-22 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20201128_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.FileField(blank=True, default='', upload_to='image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='img2',
            field=models.FileField(blank=True, default='', upload_to='image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='img3',
            field=models.FileField(blank=True, default='', upload_to='image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='img4',
            field=models.FileField(blank=True, default='', upload_to='image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='img5',
            field=models.FileField(blank=True, default='', upload_to='image'),
        ),
    ]
