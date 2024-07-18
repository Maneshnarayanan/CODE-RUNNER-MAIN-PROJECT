from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
# class ExampleModel(models.Model):
#     model_pic = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')    