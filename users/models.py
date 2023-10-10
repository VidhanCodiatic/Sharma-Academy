

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


USER_TYPE = (
   ('student' , 'Student'),
   ('instructor' , 'Instructor'),
)


class CustomUser(AbstractUser):
  
  username = None

  phone_number = models.IntegerField(unique = True)
  email = models.EmailField(unique = True)
  user_type = models.CharField(max_length = 100, choices = USER_TYPE, default = 'student')
  terms_condition = models.BooleanField()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []

  