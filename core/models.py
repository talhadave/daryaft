from ckeditor.fields import RichTextField
from django.db import models

from daryaft.users.models import User


# Create your models here.
class question(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=User)
    question_title = models.CharField(max_length=250)
    question_body = RichTextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    like = models.IntegerField(default=0)
    # tags=models.ForeignKey(tags,on_delete=models.CASCADE)

    def __str__(self):
        return self.question_title


class tags(models.Model):
    tag_slug = models.SlugField(max_length=250)
    description = models.TextField(max_length=450)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Answer(models.Model):
    question = models.ForeignKey(
        question, on_delete=models.CASCADE, blank=False, null=True
    )
    answer = RichTextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    User = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=User)
