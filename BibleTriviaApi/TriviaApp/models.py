from django.db import models

# Create your models here.

class BibleQuestion(models.Model):
    Id = models.AutoField(primary_key=True)
    Category = models.IntegerField()
    DifficultyLevel = models.IntegerField()
    QuestionInfoId = models.IntegerField()
    Answered = models.BooleanField(default=False)


class QuestionInfo(models.Model):
    Id = models.AutoField(primary_key=True)
    Question = models.CharField(max_length=100)
    Answer = models.CharField(max_length=100)