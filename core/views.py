from django.shortcuts import render


# Create your views here.
def question_view(request):
    template_name = "template/base.html"
    return render(request, template_name)


def tags_view(request):
    template_name = "template/base.html"
    return render(request, template_name)


def answer_view(request):
    template_name = "template/base.html"
    return render(request, template_name)
