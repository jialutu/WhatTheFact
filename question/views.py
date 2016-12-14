from question.models import QuestionableFact
from question.serializers import QuestionSerializer
from rest_framework import generics


class QuestionList(generics.ListCreateAPIView):
    queryset = QuestionableFact.objects.all()
    serializer_class = QuestionSerializer


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuestionableFact.objects.all()
    serializer_class = QuestionSerializer