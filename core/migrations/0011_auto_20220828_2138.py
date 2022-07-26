# Generated by Django 3.2.14 on 2022-08-28 21:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0010_question_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='upvote_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='unlike',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='downvote_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
