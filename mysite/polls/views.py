from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.db.models import F
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Question, Choice
# Create your views here.

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        # Returns the five recent questions in the future
        return Question.objects.filter(pub_date__lte = timezone.now()).order_by('pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"
    
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte = timezone.now())
class ResultView(generic.DetailView):
    model = Question
    template_name = "polls/result.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Renders back the form if any of the above errors come through
        return render(request, "polls/detail.html", {
            "question": question,
            "error_message": "Choice doesn't exist"
        })
    else:
        selected_choice.votes = F("votes") + 1 #Increments the value of votes by 1 in a database-safe way
        selected_choice.save()

        return HttpResponseRedirect(reverse("polls:results", args=(question_id,)))