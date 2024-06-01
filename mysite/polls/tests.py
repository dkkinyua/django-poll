import datetime
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
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

def create_question(question_text, days):
    # creates a question based on the above arguments and this helps us avoid writing too much code by using the DRY principle
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question=question_text, pub_date = time)

class QuestionIndexViewsTexts(TestCase):
    # Checks if there are polls, if not return appropriate message
    def test_no_questions(self):
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available now, try later")

    # Checks if the question is in the past
    def test_past_question(self):
        question = create_question(question_text = "Past Question", days=-30)
        response = self.client.get(reverse("polls:index"))

        self.assertQuerySetEqual(
            response.content["latest_question_list"],
            [question]
        )