# from django import forms
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.forms import modelformset_factory
# from django.http import Http404
from django.shortcuts import get_object_or_404, render

from core.form import questionForm
from core.models import question

# from django.views.generic.edit import View


# from daryaft.daryaft.users.views import User


# Create your views here.
def question_view(request):
    latest_question_list = question.objects.order_by("created")[:10]
    template_name = "core/question_view.html"
    context = {"latest_question_list": latest_question_list}
    return render(request, template_name, context)


def ask_question(request):
    # questionForm=modelformset_factory(question,fields=('question_title','question_body'))
    # form=questionForm()
    form = questionForm(request.POST or None)
    # if request.method=='POST':
    if form.is_valid():
        obj = form.save(commit=False)
        # form.instance.User = request.User
        # obj.question_title=form.cleaned_data.get("question_title")
        # obj.user=User .objects.get(User=self.request.User)
        obj.save()
        form = questionForm()
    context = {"form": form}
    template_name = "core/ask_question.html"
    return render(request, template_name, context)


# class ask_question(LoginRequiredMixin, View):
#     def get(self, request, *args, **kwargs):
#         form = questionForm()
#         context = {'form':form}
#         return render(request, 'core/ask_question.html', context)

#     def post(self, request, *args, **kwargs):

#         form = questionForm(request.POST)
#         form.instance.user = request.user
#         if form.is_valid():
#             form.save()
#             return redirect(reverse('core:index'))
def question_detail_view(request, question_id):
    # try:
    # questions=question.objects.all()
    #     obj=get_object_or_404(question,id=question_id)
    # except question.DoesNotExist:
    #     raise Http404
    # questions = forms.ModelMultipleChoiceField(queryset=question.objects.all(), widget=forms.CheckboxSelectMultiple)
    # latest_question_list = question.objects.order_by('created')[:10]
    # questions=question.objects.get(pk=question_id)
    # questions=question.objects.filter(pk=question_id)
    questions = get_object_or_404(question, pk=question_id)
    template_name = "core/detail_question.html"
    context = {"question": questions}
    return render(request, template_name, context)


def index_view(request):
    latest_question_list = question.objects.order_by("created")[:10]
    template_name = "core/index.html"
    context = {"latest_question_list": latest_question_list}
    return render(request, template_name, context)


def tags_view(request):
    template_name = "core/title.html"
    # question_title=request.GET.get('text','default')
    # context={'purpose':'title','question_title':question_title}
    return render(request, template_name)


def answer_view(request):
    template_name = "base.html"
    return render(request, template_name)
