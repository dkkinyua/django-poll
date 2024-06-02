import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin

# Create your models here.

# Question model
class Question(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    # returns a string representation of "question"
    def __str__(self):
        return self.question
    
    @admin.display(
            boolean= True,
            ordering="pub_date",
            description="Published recently?"
    )
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
# Choice model 
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #ForeignKey - Question & Choice(One-to-many)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # returns a string representation of "choice_text"
    def __str__(self):
        return self.choice_text