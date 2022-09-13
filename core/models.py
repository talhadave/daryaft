from ckeditor.fields import RichTextField
from django.db import models
from taggit.managers import TaggableManager

from daryaft.users.models import User


# Create your models here.
class question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=User)
    question_title = models.CharField(max_length=250)
    question_body = RichTextField(max_length=20000)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=100)
    modified = models.DateTimeField(auto_now=True)
    tags = TaggableManager()
    upvotes = models.ManyToManyField(User, related_name="upvotes")
    downvotes = models.ManyToManyField(User, related_name="downvotes")

    def __str__(self):
        return self.question_title

    def total_upvotes(self):
        return self.upvotes.count()

    def total_downvotes(self):
        return self.downvotes.count()

    def total_votes(self):
        return self.upvotes.count() - self.downvotes.count()


class Answer(models.Model):
    question = models.ForeignKey(
        question, on_delete=models.CASCADE, blank=False, null=True
    )
    answer = RichTextField(max_length=10000)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=User)
    upvotes = models.ManyToManyField(User, related_name="answer_upvotes")
    downvotes = models.ManyToManyField(User, related_name="answer_downvotes")

    def __str__(self):
        return self.answer

    def total_upvotes(self):
        return self.upvotes.count()

    def total_downvotes(self):
        return self.downvotes.count()

    def total_votes(self):
        return self.upvotes.count() - self.downvotes.count()


class questionComment(models.Model):
    question = models.ForeignKey(
        question, on_delete=models.CASCADE, related_name="question_comments"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(default="")
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment


class answerComment(models.Model):
    answer = models.ForeignKey(
        Answer, on_delete=models.CASCADE, related_name="answer_comments"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(default="")
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment
