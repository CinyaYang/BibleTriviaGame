from rest_framework import serializers
from TriviaApp.models import BibleQuestion, QuestionInfo

class BibleQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BibleQuestion
        fields = ('Id',
                  'Category',
                  'DifficultyLevel',
                  'QuestionInfoId',
                  'Answered')

class QuestionInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionInfo
        fields = ('Id',
                  'Question',
                  'Answer')