from django.db import models

from daryaft.users.models import User


# Create your models here.
class question(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    question_title = models.CharField(max_length=250)
    question_body = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    like = models.IntegerField(default=0)


class tags(models.Model):
    tag_slug = models.SlugField(max_length=250)
    description = models.TextField(max_length=450)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Answer(models.Model):
    question_id = models.ForeignKey(
        question, on_delete=models.CASCADE, blank=False, null=True
    )
    answer = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
