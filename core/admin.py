from django.contrib import admin

from core.models import Answer, answerComment, question, questionComment

# Register your models here.
admin.site.register(question)
admin.site.register(Answer)
admin.site.register(questionComment)
admin.site.register(answerComment)
