  

from django.db import models
from django.contrib.auth.models import AbstractUser
from users.managers import CustomUserManager

TYPE = (
   ('admin' , 'Admin'),
   ('student' , 'Student'),
   ('instructor' , 'Instructor'),
)


class CustomUser(AbstractUser):

   username = None
   
   phone = models.IntegerField(unique = True, null = True)
   email = models.EmailField(unique = True)
   password = models.CharField(max_length = 255)
   type = models.CharField(max_length = 100, 
                                choices = TYPE, default = 'Student')

   USERNAME_FIELD = 'email'
   REQUIRED_FIELDS = []
    
   objects = CustomUserManager()

   def __str__(self):
      return self.email