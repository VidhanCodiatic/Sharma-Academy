
from django.db import models
from ..users.models import MyUser
from ..courses.models import MyCourses

# Create your models here.

ASSESSMENT_TYPE = (
    ('mcq', 'MCQ'),
    ('short_answer', 'Short_Answer'),
    ('essay', 'Essay'),
)

class Assessment(models.Model):

    assessment_for = models.ForeignKey(MyCourses, on_delete = models.CASCADE)
    assessment_title = models.CharField(max_length = 100)
    content_duration = models.CharField(max_length = 100)
    assessment_type = models.CharField(max_length = 100, 
                                 choices = ASSESSMENT_TYPE, default = 'mcq')
