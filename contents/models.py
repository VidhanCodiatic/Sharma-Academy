
from django.db import models
from ..users.models import CustomUser
from ..courses.models import MyCourses

# Create your models here.

CONTENT_TYPE = (
    ('video', 'Video'),
    ('images', 'Images'),
    ('docx', 'Docx'),
)

class Content(models.Model):

    course_for = models.ForeignKey(MyCourses, on_delete = models.CASCADE)
    content_title = models.CharField(max_length = 100)
    content_duration = models.CharField(max_length = 100)
    mode_type = models.CharField(max_length = 100, 
                                 choices = CONTENT_TYPE, default = 'docx')