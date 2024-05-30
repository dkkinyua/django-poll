from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5] # Returns the first 5 questions
    output = ", ".join([q.question for q in latest_question_list])
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("You are looking at question %s" % question_id)

def result(request, question_id):
    response = "You are looking at the results for question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting for question %s" % question_id)
