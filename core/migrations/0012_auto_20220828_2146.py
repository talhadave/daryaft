# Generated by Django 3.2.14 on 2022-08-28 21:46

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0011_auto_20220828_2138'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='unlike',
            new_name='DownVote',
        ),
        migrations.RenameModel(
            old_name='like',
            new_name='UpVote',
        ),
    ]
