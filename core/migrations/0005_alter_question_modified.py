# Generated by Django 3.2.14 on 2022-07-28 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20220728_0212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]