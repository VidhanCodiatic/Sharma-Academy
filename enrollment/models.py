
from django.db import models
from ..users.models import MyUser


class Enrollment(models.Model):

    enrollment_for = models.ForeignKey(MyUser, on_delete = models.CASCADE)
    enrollment_no = models.IntegerField(unique = True)
    created_at = 
    date = models