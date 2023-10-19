
from django.db import models
from courses.models import Course

# Create your models here.

ASSESSMENT_TYPE = (
    ('mcq', 'MCQ'),
    ('short_answer', 'Short_Answer'),
    ('essay', 'Essay'),
)

class Assessment(models.Model):

    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    title = models.CharField(max_length = 100)
    duration = models.CharField(max_length = 100)
    type = models.CharField(max_length = 100, 
                                 choices = ASSESSMENT_TYPE, default = 'mcq')
    
    def __str__(self):
        return self.title
    
class Question(models.Model):

    assessment = models.ForeignKey(Assessment, on_delete = models.CASCADE)
    question = models.CharField(max_length = 255)

    def __str__(self):
        return self.question
    
class Choice(models.Model):

    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    option = models.CharField(max_length = 200)
    correct = models.BooleanField(default = False)

    def __str__(self):
        return self.option

class Answer(models.Model):

    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    content = models.TextField(blank=True)