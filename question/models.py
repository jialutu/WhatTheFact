from django.db import models

class QuestionableFact(models.Model):
    questionable_fact = models.CharField(max_length=100)
    user_question= models.CharField(max_length=500)
    questionable_fact_url= models.CharField(max_length=200)
    user_email = models.CharField(max_length=100)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.questionable_fact