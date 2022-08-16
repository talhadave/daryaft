from django import forms

from core.models import Answer, question


class questionForm(forms.ModelForm):
    class Meta:
        model = question
        fields = [
            "question_title",
            "question_body",
        ]
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
