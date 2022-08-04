from django.shortcuts import HttpResponse


# Create your views here.
def question_view(request):
    return HttpResponse("<h1> this is my question view</h1>")


def tags_view(request):
    return HttpResponse("<h1> this is my tagsview</h1>")


def answer_view(request):
    return HttpResponse("<h1> this is my answer view</h1>")
