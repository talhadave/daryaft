# Generated by Django 3.2.14 on 2022-08-01 14:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0006_auto_20220728_0217'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='like',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='question',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_slug', models.SlugField(max_length=250)),
                ('description', models.TextField(max_length=450)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(max_length=1000)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('question_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]