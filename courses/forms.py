from courses.models import Lecture
from django import forms

class LectureForm(forms.ModelForm):

    class Meta:
        model = Lecture
        fields = '__all__'