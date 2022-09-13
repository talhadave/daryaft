from django import forms

from core.models import Answer, answerComment, question, questionComment


class questionForm(forms.ModelForm):
    class Meta:
        model = question
        fields = [
            "question_title",
            "question_body",
            "tags",
        ]
        widgets = {
            "question_title": forms.TextInput(
                attrs={"placeholder": "Title...", "class": "form-control"}
            ),
        }
        exclude = [
            "User",
        ]


class answerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = [
            "answer",
        ]
        exclude = ["User", "question"]


class questionCommentForm(forms.ModelForm):
    class Meta:
        model = questionComment
        fields = [
            "comment",
        ]
        exclude = ["User", "question"]


class answerCommentForm(forms.ModelForm):
    class Meta:
        model = answerComment
        fields = [
            "comment",
        ]
        exclude = ["User", "answer"]
