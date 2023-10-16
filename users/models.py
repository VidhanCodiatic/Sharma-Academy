  

from django.db import models
from django.contrib.auth.models import AbstractUser
from users.managers import CustomUserManager

USER_TYPE = (
   ('admin' , 'Admin'),
   ('student' , 'Student'),
   ('instructor' , 'Instructor'),
)


class CustomUser(AbstractUser):

   username = None
   
   phone_number = models.IntegerField(unique = True, null = True)
   email = models.EmailField(unique = True)
   user_type = models.CharField(max_length = 100, 
                                choices = USER_TYPE, default = 'Admin')

   USERNAME_FIELD = 'email'
   REQUIRED_FIELDS = []
    
   objects = CustomUserManager()

   def __str__(self):
      return self.email