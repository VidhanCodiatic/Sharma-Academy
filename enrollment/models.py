
from users.models import CustomUser
from django.db import models

    
class Enrollment(models.Model):

    enrollment_for = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    enrollment_no = models.IntegerField(default = 101, editable = False)
    date = models.DateTimeField(auto_now_add = True)
    update = models.DateTimeField(auto_now = True)

    def save(self, *args, **kwargs):
        if not self.pk:
            last_instance = Enrollment.objects.last()
            if last_instance:
                self.enrollment_no = last_instance.enrollment_no + 1
            super(Enrollment, self).save(*args, **kwargs)