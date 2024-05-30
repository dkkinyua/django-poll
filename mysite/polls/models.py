from django.db import models
from django.utils import timezone

# Create your models here.

# Question model
class Question(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    # returns a string representation of "question"
    def __str__(self):
        return self.question
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - timezone.timedelta(days=1)

# Choice model 
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #ForeignKey - Question & Choice(One-to-many)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # returns a string representation of "choice_text"
    def __str__(self):
        return self.choice_text