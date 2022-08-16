# Generated by Django 3.2.14 on 2022-08-16 02:21

import builtins
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_alter_answer_question_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='question_id',
            field=models.ForeignKey(default=builtins.id, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.question'),
        ),
    ]