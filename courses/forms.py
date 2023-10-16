from courses.models import Lecture, EmbedLecture, Document, Pdf
from django import forms

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