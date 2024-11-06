from django.db import models
import datetime
from django.utils import timezone

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    # Returns question string
    def __str__(self):  
        return self.question_text
    # Sets publication date to current day.
    def date_publication(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text


    # Change your models (in models.py).

# Run python manage.py makemigrations to create migrations for those changes

# Run python manage.py migrate to apply those changes to the database.