from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import HttpResponseRedirect, get_object_or_404, redirect, render
from django.urls import reverse
from taggit.models import Tag

from core.form import answerForm, questionForm
from core.models import Answer, answerComment, question, questionComment
from daryaft.users.models import User


def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    common_tags = question.tags.most_common()[:15]
    questions = question.objects.filter(tags=tag)
    context = {
        "tag": tag,
        "common_tags": common_tags,
        "questions": questions,
    }
    return render(request, "core/question_by_tags.html", context)


def all_users(request):
    users = User.objects.all()
    context = {"users": users}
    return render(request, "users/all_users.html", context)


def tags_list_view(request):
    tags = Tag.objects.all()
    context = {"tags": tags}
    return render(request, "core/tags_list.html", context)


def question_view(request):
    latest_question_list = question.objects.order_by("-created")
    template_name = "core/question_view.html"
    context = {"latest_question_list": latest_question_list}
    return render(request, template_name, context)


@login_required
def ask_question(request):
    form = questionForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form.save_m2m()
        return redirect(reverse("detail", kwargs={"question_id": obj.id}))
    context = {"form": form}
    template_name = "core/ask_question.html"
    return render(request, template_name, context)


@login_required
def edit_question(request, question_id=None):
    if question_id:

        questions = get_object_or_404(question, pk=question_id)
        form = questionForm(instance=questions)
        if request.user == questions.user:
            if request.method == "POST":
                form = questionForm(request.POST, instance=questions)
                if form.is_valid():
                    form.save()
                return redirect(reverse("detail", kwargs={"question_id": questions.id}))
        else:
            messages.success(request, "You are not able to edit it.")
            return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))
    context = {"form": form}
    template_name = "core/edit_question.html"
    return render(request, template_name, context)


@login_required
def edit_answer(request, answer_id=None):
    if answer_id:
        answers = get_object_or_404(Answer, pk=answer_id)
        form = answerForm(instance=answers)
        if request.user == answers.user:
            if request.method == "POST":
                form = answerForm(request.POST, instance=answers)
                if form.is_valid():
                    form.save()
                return redirect("/")
        else:
            messages.success(request, "You are not able to edit it.")
            return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))
    context = {"form": form}
    template_name = "core/edit_answer.html"
    return render(request, template_name, context)


def question_detail_view(request, question_id):
    quest = question.objects.get(pk=question_id)
    tags = quest.tags.all()
    answers = Answer.objects.filter(question=quest)
    latest_comments_question = questionComment.objects.order_by("-add_time")
    latest_comments_answer = answerComment.objects.order_by("-add_time")
    comments = questionComment.objects.filter(pk=question_id)
    answerform = answerForm(request.POST or None)
    if answerform.is_valid():
        obj = answerform.save(commit=False)
        obj.question = quest
        obj.user = request.user
        obj.save()
        answerform.cleaned_data["answer"]
        answerform = answerForm()
    context = {
        "quest": quest,
        "tags": tags,
        "answers": answers,
        "answerform": answerform,
        "question": question,
        "comments": comments,
        "latest_comments_question": latest_comments_question,
        "latest_comments_answer": latest_comments_answer,
    }
    template_name = "core/detail_question.html"
    return render(request, template_name, context)


def answer_view(request, question_id):
    latest_question_list = Answer.objects.filter(question=question_id).order_by(
        "-created"
    )
    template_name = "core/detail_question.html"
    context = {"latest_question_list": latest_question_list}
    return render(request, template_name, context)


def ask_comment_questiom(request):
    cmnt_body = str(request.GET.get("cmnt_body"))
    cmnt_username = request.user
    post = get_object_or_404(question, id=request.GET.get("question_id"))
    print(post)
    print(cmnt_body, cmnt_username, post)
    questionComment.objects.create(question=post, comment=cmnt_body, user=cmnt_username)
    cmnt = (
        questionComment.objects.filter(question=post, user=cmnt_username)
        .order_by()
        .last()
    )
    response = {
        "cmnt_username": cmnt.user.username,
        "cmnt_body": cmnt.comment,
        "cmnt_add_time": cmnt.add_time.date(),
    }
    return JsonResponse(response)


def ask_comment_answer(request):
    cmnt_body = str(request.GET.get("cmnt_body"))
    cmnt_username = request.user
    post = get_object_or_404(Answer, id=request.GET.get("answer_id"))
    print(post)
    print(cmnt_body, cmnt_username, post)
    answerComment.objects.create(answer=post, comment=cmnt_body, user=cmnt_username)
    cmnt = answerComment.objects.filter(answer=post, user=cmnt_username).last()
    response = {
        "cmnt_username": cmnt.user.username,
        "cmnt_body": cmnt.comment,
        "cmnt_add_time": cmnt.add_time.date(),
    }
    return JsonResponse(response)


def LikeView(request):
    questions = get_object_or_404(question, id=request.GET.get("question_id"))
    if request.GET.get("vote_type") == "upvote":
        if questions.downvotes.filter(id=request.user.id).exists():
            questions.downvotes.remove(request.user)
            questions.upvotes.add(request.user)
        elif questions.upvotes.filter(id=request.user.id).exists():
            questions.upvotes.remove(request.user)
        else:
            questions.upvotes.add(request.user)
    elif request.GET.get("vote_type") == "downvote":
        if questions.upvotes.filter(id=request.user.id).exists():
            questions.upvotes.remove(request.user)
            questions.downvotes.add(request.user)
        elif questions.downvotes.filter(id=request.user.id).exists():
            questions.downvotes.remove(request.user)
        else:
            questions.downvotes.add(request.user)
    response = {"total_votes": questions.total_votes()}
    return JsonResponse(response)


def AnswerLikeView(request):
    answers = get_object_or_404(Answer, id=request.GET.get("answer_id"))
    if request.GET.get("vote_type") == "upvote":
        if answers.downvotes.filter(id=request.user.id).exists():
            answers.downvotes.remove(request.user)
            answers.upvotes.add(request.user)
        elif answers.upvotes.filter(id=request.user.id).exists():
            answers.upvotes.remove(request.user)
        else:
            answers.upvotes.add(request.user)
    elif request.GET.get("vote_type") == "downvote":
        if answers.upvotes.filter(id=request.user.id).exists():
            answers.upvotes.remove(request.user)
            answers.downvotes.add(request.user)
        elif answers.downvotes.filter(id=request.user.id).exists():
            answers.downvotes.remove(request.user)
        else:
            answers.downvotes.add(request.user)
    response = {"total_votes": answers.total_votes()}
    return JsonResponse(response)
