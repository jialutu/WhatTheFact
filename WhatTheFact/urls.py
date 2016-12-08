"""WhatTheFact URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from question.models import QuestionableFact
from question import views

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QuestionableFact
        fields = ('questionable_fact', 'user_question', 'questionable_fact_url', 'created_time')

# ViewSets define the view behavior.
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = QuestionableFact.objects.all()
    serializer_class = QuestionSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'questions', QuestionViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^questions/$', views.question_list),
    url(r'^questions/(?P<pk>[0-9]+)$', views.question_list),
]

# urlpatterns = format_suffix_patterns(urlpatterns)