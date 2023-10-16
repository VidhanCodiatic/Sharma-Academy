from django.contrib import admin
from courses.models import Course, Lecture, EmbedLecture

# Register your models here.

admin.site.register(Course)
admin.site.register(Lecture)
admin.site.register(EmbedLecture)

