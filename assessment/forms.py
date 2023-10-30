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
        # fields = ['content']
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        user = self.request.user
        self.fields['user'].queryset = Answer.objects.filter(user = user)
        
    # def __init__(self, *args, **kwargs):
    #     super(AnswerForm, self).__init__(*args, **kwargs)
    #     self.fields['question'].queryset = Assessment.objects.filter(type = 'short_answer')
        # widgets = {
        #     'content': forms.Textarea(attrs={'name':'content[]'}),
        # }