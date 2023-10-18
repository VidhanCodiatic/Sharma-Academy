from courses.models import Course, Lecture, EmbedLecture, Document, Pdf
from django import forms
from users.models import CustomUser


class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        self.fields['instructor'].queryset = CustomUser.objects.filter(user_type = 'instructor')


class LectureForm(forms.ModelForm):

    class Meta:
        model = Lecture
        fields = '__all__'

class PdfForm(forms.ModelForm):

    class Meta:
        model = Pdf
        fields = '__all__'

class EmbedLectureForm(forms.ModelForm):

    class Meta:
        model = EmbedLecture
        fields = '__all__'

class DocumentForm(forms.ModelForm):

    class Meta:
        model = Document
        fields = '__all__'