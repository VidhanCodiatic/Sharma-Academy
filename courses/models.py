

from django.db import models
from ..users.models import MyUser

# Create your models here.

DURATION = (
    ('1 year', '1 year'),
    ('6 months', '6 months'),
    ('3 months', '3 months'),
)

MODE_TYPE = (
    ('online', 'Online'),
    ('blended', 'Blended'),
    ('offline', 'Offline'),
)

class Course(models.Model):

    course_name = models.CharField(max_length = 100)
    course_duration = models.CharField(max_length = 100, 
                                       choices = DURATION, default = '3 months')
    course_fees = models.IntegerField()
    mode_type = models.CharField(max_length = 100, 
                                 choices = MODE_TYPE, default = 'offline')