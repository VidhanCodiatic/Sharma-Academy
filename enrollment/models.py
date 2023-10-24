
from users.models import CustomUser
from django.db import models

    
class Enrollment(models.Model):

    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    enroll_no = models.IntegerField(default = 101, editable = False)
    date = models.DateTimeField(auto_now_add = True)
    update = models.DateTimeField(auto_now = True)

    def save(self, *args, **kwargs):
        if not self.pk:
            last_instance = Enrollment.objects.last()
            if last_instance:
                self.enroll_no = last_instance.enroll_no + 1
            super(Enrollment, self).save(*args, **kwargs)