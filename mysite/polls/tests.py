import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Question

# Create your tests here.
class QuestionModelTests(TestCase):
    def test_was_question_published_recently(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_time = Question(pub_date=time)

        self.assertIs(future_time.was_published_recently(), False)
    # Should bring False if the post is older than one day
    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)

        self.assertIs(old_question.was_published_recently(), False)

    # Should return true if the pub_date is less or between a day
    def test_was_question_recently_with_new_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        new_question = Question(pub_date = time)

        self.assertIs(new_question.was_published_recently(), True)
