# Generated by Django 2.2.12 on 2020-12-07 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_comment', '0003_auto_20201130_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_comment',
            name='parent_message',
            field=models.IntegerField(null=True, verbose_name='父留言'),
        ),
    ]
