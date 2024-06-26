from django.urls import path
from . import views

# Maps these URLS to different views on views.py.
app_name = 'polls'
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"), # /polls/
    path("<int:pk>/", views.DetailView.as_view(), name="detail"), # example, /polls/5(question_id)/
    path("<int:pk>/results/", views.ResultView.as_view(), name="results"), #/polls/5/results/
    path("<int:question_id>/vote", views.vote, name="vote") #/polls/5/vote
]