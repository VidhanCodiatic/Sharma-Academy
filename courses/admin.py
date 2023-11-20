

from django.contrib import admin

from courses.models import (
    Course,
    Lecture,
    EmbedLecture,
    Pdf,
    Document
)

from courses.forms import (
    CourseForm,
    LectureForm,
    PdfForm,
    EmbedLectureForm,
    DocumentForm
)

# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    form = CourseForm


admin.site.register(Course, CourseAdmin)


class LectureAdmin(admin.ModelAdmin):
    form = LectureForm


admin.site.register(Lecture, LectureAdmin)


class PdfAdmin(admin.ModelAdmin):
    form = PdfForm


admin.site.register(Pdf, PdfAdmin)


class EmbedAdmin(admin.ModelAdmin):
    form = EmbedLectureForm


admin.site.register(EmbedLecture, EmbedAdmin)


class DoxAdmin(admin.ModelAdmin):
    form = DocumentForm


admin.site.register(Document, DoxAdmin)
