

from django.db import models
from users.models import CustomUser

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

    instructor = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    name = models.CharField(max_length = 100, unique = True)
    image = models.ImageField(upload_to = 'course')
    duration = models.CharField(max_length = 100, 
                                       choices = DURATION, default = '3 months')
    fees = models.IntegerField()
    mode_type = models.CharField(max_length = 100, 
                                 choices = MODE_TYPE, default = 'offline')
    description = models.CharField(max_length = 255)
    
    def __str__(self) -> str:
        return self.name

class Lecture(models.Model):

    upload_by = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    title = models.CharField(max_length = 100, unique = True)    
    duration = models.CharField(max_length = 100)
    lecture = models.FileField(upload_to = 'lectures/')
    
    def __str__(self):
        return self.title
    
class Pdf(models.Model):

    upload_by = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    title = models.CharField(max_length = 100)    
    page = models.IntegerField()
    pdfFile = models.FileField(upload_to = 'files/')
    
    def __str__(self):
        return self.title

class EmbedLecture(models.Model):

    upload_by = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    title = models.CharField(max_length = 100)
    duration = models.CharField(max_length = 100)
    lectureUrl = models.URLField()

    def __str__(self):
        return self.title
    
class Document(models.Model):

    upload_by = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    title = models.CharField(max_length = 100)
    documentUrl = models.URLField()

    def __str__(self):
        return self.title