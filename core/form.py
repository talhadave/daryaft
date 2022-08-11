from django import forms

from core.models import question


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
