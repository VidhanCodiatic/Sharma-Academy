from django.contrib import admin

from assessment.models import Assessment, Question, Rating

# Register your models here.

admin.site.register(Assessment)
admin.site.register(Question)
admin.site.register(Rating)
