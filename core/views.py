from django.forms import modelformset_factory
from django.shortcuts import get_object_or_404, render

from core.form import answerForm, questionForm
from core.models import question


# Create your views here.
def question_view(request):
    latest_question_list = question.objects.order_by("created")[:10]
    template_name = "core/question_view.html"
    context = {"latest_question_list": latest_question_list}
    return render(request, template_name, context)


def ask_question(request):
    form = questionForm(request.POST or None)
    # if request.method=='POST':
    if form.is_valid():
        obj = form.save(commit=False)
        # form.instance.User = request.User
        current_user = request.user
        print(current_user.id)
        # obj.question_title=form.cleaned_data.get("question_title")
        # obj.user=User .objects.get(User=self.request.User)
        obj.save()
        form = questionForm()
    context = {"form": form}
    template_name = "core/ask_question.html"
    return render(request, template_name, context)


def edit_question(request, question_id):
    questions = get_object_or_404(question, pk=question_id)
    AuthorFormSet = modelformset_factory(
        question, fields=("question_title", "question_body")
    )
    queryset = question.objects.filter(id=question_id)
    if request.method == "POST":
        formset = AuthorFormSet(
            request.POST,
            request.FILES,
            queryset=queryset,
        )
        if formset.is_valid():
            formset.save()
            # Do something.
    else:
        formset = AuthorFormSet(queryset=queryset)
    return render(
        request, "core/edit_question.html", {"formset": formset, "question": questions}
    )


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


def ask_answer(request, question_id):
    questions = get_object_or_404(question, pk=question_id)
    form = answerForm(request.POST or None)
    # if request.method=='POST':
    if form.is_valid():
        obj = form.save(commit=False)
        # form.question= question.objects.filter(id=question_id)
        # current_question=request.question_id
        current_user = request.user
        print(current_user.id)
        # form.instance.User = request.User
        # obj.question_title=form.cleaned_data.get("question_title")
        # obj.user=User .objects.get(User=self.request.User)
        obj.save()
        form = answerForm()
    context = {"form": form, "question": questions}
    template_name = "core/answer.html"
    return render(request, template_name, context)


# def answer_view(request, question_id):
#     latest_question_list = Answer.objects.filter(question=question_id).order_by(
#         "created"
#     )[:10]
#     template_name = "core/answer_view.html"
#     context = {"latest_question_list": latest_question_list}
#     return render(request, template_name, context)
