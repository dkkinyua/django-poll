from django.urls import path
from . import views

# Maps these URLS to different views on views.py.
app_name = 'polls'
urlpatterns = [
    path("", views.index, name="index"), # /polls/
    path("<int:question_id>/", views.detail, name="detail"), # example, /polls/5(question_id)/
    path("<int:question_id>/results/", views.result, name="results"), #/polls/5/results/\
    path("<int:question_id>/vote", views.vote, name="vote") #/polls/5/vote
]