from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Question
# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5] # Returns the first 5 questions
    # template = loader.get_template("polls/index.html"), we no longer need loader as we'll use render()
    context = {
        "latest_question_list": latest_question_list # Returns latest_question_list as a Python object to use
    }
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id) # Gets the requested object, or returns a 404 error
    return render(request, "polls/detail.html", {"question": question}) # Same as context = {"question": question}

def result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/result.html", {"question": question})

def vote(request, question_id):
    return HttpResponse("You are voting for question %s" % question_id)
