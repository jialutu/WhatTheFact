from rest_framework import serializers, viewsets
from .models import QuestionableFact


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionableFact
        fields = ('questionable_fact', 'user_question', 'questionable_fact_url', 'user_email')

