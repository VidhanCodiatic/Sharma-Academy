from django import forms
from assessment.models import Assessment, Question, Choice, Answer
from users.models import CustomUser

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
        # fields = ['content']
        fields = '__all__'
        # exclude = ('user',)

    # def __init__(self, *args, **kwargs):
    #     # self.request = kwargs.pop('request')
    #     super(AnswerForm, self).__init__(*args, **kwargs)

            
    # def __init__(self, *args, **kwargs):
    #     super(AnswerForm, self).__init__(*args, **kwargs)
    #     self.fields['user'].queryset = CustomUser.objects.filter(type = 'instructor')