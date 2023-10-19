from django import forms
from assessment.models import Assessment, Question, Choice, Answer

class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = '__all__'

class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = '__all__'