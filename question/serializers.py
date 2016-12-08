from rest_framework import serializers
from .models import QuestionableFact


class QuestionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    questionable_fact = serializers.CharField(max_length=100)
    user_question= serializers.CharField(max_length=500)
    questionable_fact_url= serializers.CharField(max_length=200)
    user_email = serializers.CharField(max_length=100)
    created_time = serializers.DateTimeField()

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return QuestionableFact.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.questionable_fact = validated_data.get('questionable_fact', instance.title)
        instance.user_question = validated_data.get('user_question', instance.code)
        instance.questionable_fact_url = validated_data.get('questionable_fact_url', instance.linenos)
        instance.user_email = validated_data.get('user_email', instance.language)
        instance.created_time = validated_data.get('created_time', instance.style)
        instance.save()
        return instance