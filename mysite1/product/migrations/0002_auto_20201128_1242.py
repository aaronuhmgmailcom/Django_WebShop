# Generated by Django 2.2.12 on 2020-11-28 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img2',
            field=models.FileField(default='', upload_to='productImages'),
        ),
        migrations.AddField(
            model_name='product',
            name='img3',
            field=models.FileField(default='', upload_to='productImages'),
        ),
        migrations.AddField(
            model_name='product',
            name='img4',
            field=models.FileField(default='', upload_to='productImages'),
        ),
        migrations.AddField(
            model_name='product',
            name='img5',
            field=models.FileField(default='', upload_to='productImages'),
        ),
    ]
