# Generated by Django 3.2.14 on 2022-08-16 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_remove_question_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='like',
            field=models.IntegerField(default=0),
        ),
    ]