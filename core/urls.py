# enter yore url
from django.urls import path

from core.views import ask_question, edit_answer, edit_question, question_detail_view

urlpatterns = [
    path("ask/", ask_question, name="ask_question"),
    path("<int:question_id>/", question_detail_view, name="detail"),
    path("<int:question_id>/edit/", edit_question, name="edit_question"),
    path("answer/<int:answer_id>/edit/", edit_answer, name="edit_answer"),
]
