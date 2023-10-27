from django.shortcuts import render, redirect
from django.http import HttpResponse
from assessment.models import Question, Choice
from assessment.forms import QuestionForm, AnswerForm, AssessmentForm, ChoiceForm
from django.views import View
from django.forms import formset_factory


class AssessmentView(View):

    " Define assessment type and course "

    form_class = AssessmentForm
    template_name = 'assessment/addassessment.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form' : form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        user = request.user

        if user.type == 'instructor':
            if form.is_valid():
                form.save()
                return HttpResponse('added')
            else:
                return HttpResponse('not valid form')
        else:
            return HttpResponse('not instructor')


class QuestionView(View):

    " Adding questions for assessment "

    form_class = QuestionForm
    template_name = "assessment/addQuestion.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form' : form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        user = request.user

        if user.type == 'instructor':
            if form.is_valid():
                form.save()
                return HttpResponse('added')
            else:
                return HttpResponse('not valid form')
        else:
            return HttpResponse('not instructor')


class ChoiceView(View):

    " Adding questions for assessment "

    form_class = ChoiceForm
    template_name = "assessment/addChoice.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form' : form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        user = request.user

        if user.type == 'instructor':
            if form.is_valid():
                form.save()
                return HttpResponse('added')
            else:
                return HttpResponse('not valid form')
        else:
            return HttpResponse('not instructor')


class QuizView(View):

    " Generate score for particular assessment "

    form_class = AnswerForm
    template_name = "assessment/quiz.html"

    def get(self, request, *args, **kwargs):
        AnswerFormSet = formset_factory(AnswerForm)
        formset = AnswerFormSet()
        # form = self.form_class()
        questions = Question.objects.all()
        return render(request, self.template_name, {'questions' : questions, 'formset' : formset})
    
    def post(self, request, *args, **kwargs):
        score = 0
        for q in Question.objects.all():
            select_option_id = request.POST.get(f'q_{q.id}')
            if select_option_id:
                select_option = Choice.objects.get(pk=select_option_id)
                if select_option.correct:
                    score += 1

        return render(request, 'assessment/score.html', {'score' : score})



class TextquizView(View):

    " Generate score for particular assessment "

    form_class = AnswerForm
    template_name = "assessment/text_quiz.html"

    def get(self, request, *args, **kwargs):
        AnswerFormSet = formset_factory(AnswerForm)
        formset = AnswerFormSet()
        # form = self.form_class()
        questions = Question.objects.all()
        return render(request, self.template_name, {'questions' : questions, 'formset' : formset})


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
