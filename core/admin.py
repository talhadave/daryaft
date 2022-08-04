from django.contrib import admin

from core.models import Answer, question, tags

# Register your models here.
admin.site.register(question)
admin.site.register(tags)
admin.site.register(Answer)
