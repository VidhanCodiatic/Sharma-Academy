from django.shortcuts import render, redirect
from django.http import HttpResponse
from assessment.models import Question, Choice
from assessment.forms import QuestionForm, AnswerForm
from django.views import View


class QuestionView(View):

    form_class = QuestionForm
    template_name = "assessment/addQuestion.html"

    def get(self,request, *args, **kwargs):
        question_form = self.form_class()
        return render(request, self.template_name, {'question_form' : question_form})
    
    def post(self, request, *args, **kwargs):
        question_form = self.form_class()

        # uploader = 


class QuizView(View):

    form_class = AnswerForm
    template_name = "assessment/quiz.html"

    def get(self, request, *args, **kwargs):
        AnswerFormSet = formset_factory(AnswerForm, extra=5)
        formset = AnswerFormSet()
        form = self.form_class()
        questions = Question.objects.all()
        return render(request, self.template_name, {'questions' : questions, 'form' : form,
                                                    'formset' : formset})
    
    def post(self, request, *args, **kwargs):
        score = 0
        for q in Question.objects.all():
            select_option_id = request.POST.get(f'q_{q.id}')
            if select_option_id:
                select_option = Choice.objects.get(pk=select_option_id)
                if select_option.correct:
                    score += 1

        return render(request, 'assessment/score.html', {'score' : score})


# blog/views.py
from django.forms import formset_factory

def create_multiple_content(request):
    AnswerFormSet = formset_factory(AnswerForm, extra=5)
    formset = AnswerFormSet()
    if request.method == 'POST':
            formset = AnswerFormSet(request.POST, request.FILES)
            if formset.is_valid():
                for form in formset:
                    if form.cleaned_data:
                        content = form.save(commit=False)
                        content.uploader = request.content
                        content.save()
                return HttpResponse('created')
    return render(request, 'assessment/quiz.html', {'formset': formset})



# class PublicationCreateView(EdqmCreateView):
#     """ Create publication with document form through formset """
#     model = Publication
#     template_name = 'freepub/publication/publication_form.html'

#     def get_context_data(self, **kwargs):
#         context = super(PublicationCreateView, self).get_context_data(**kwargs)
#         context['DocumentFormSets'] = DocumentFormSets(self.request.POST or None, self.request.FILES or None)
#         return context

#     def form_valid(self, form):
#         context = self.get_context_data()
#         formsets = context['DocumentFormSets']
#         if form.is_valid() and formsets.is_valid():
#             self.object = form.save()
#             formsets.instance = self.object
#             formsets.save()
#         return super(PublicationCreateView, self).form_valid(form)
