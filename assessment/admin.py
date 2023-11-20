from django.contrib import admin

from assessment.models import (
    Assessment,
    Question,
    Choice,
    Answer,
    Rating
)

# Register your models here.

admin.site.register(Assessment)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Answer)
admin.site.register(Rating)
