from django.contrib import admin
from courses.models import Course, Lecture, EmbedLecture
from courses.forms import CourseForm

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    form = CourseForm

admin.site.register(Course, CourseAdmin)

admin.site.register(Lecture)
admin.site.register(EmbedLecture)

