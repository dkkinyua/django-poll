from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello, you are at the polls index.")

def detail(request, question_id):
    return HttpResponse("You are looking at question %s" % question_id)

def result(request, question_id):
    response = "You are looking at the results for question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting for question %s" % question_id)
