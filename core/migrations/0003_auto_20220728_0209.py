# Generated by Django 3.2.14 on 2022-07-28 02:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20220728_0155'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='question',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
