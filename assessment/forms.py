from django import forms
from assessment.models import Assessment, Question, Choice, Answer

class AssessmentForm(forms.ModelForm):

    class Meta:
        model = Assessment
        fields = '__all__'

class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = '__all__'

class ChoiceForm(forms.ModelForm):

    class Meta:
        model = Choice
        fields = '__all__'

class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = '__all__'
        widgets = {
            'content': forms.Textarea(attrs={'name':'content[]'}),
        }