from django.shortcuts import render, redirect
from django.http import HttpResponse
from assessment.models import Assessment, Question, Choice, Answer
from assessment.forms import QuestionForm, AnswerForm, AssessmentForm, ChoiceForm
from django.views import View
from django.forms import modelformset_factory

from functools import partial as curry

class ShowAssessmentView(View):

    " Showing all assessment present in project "

    template_name = 'assessment/assessment.html'

    def get(self, request, *args, **kwargs):
        assessment = Assessment.objects.all()
        return render(request, self.template_name, {'assessment' : assessment})


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


# class QuizView(View):

#     " Generate score for particular assessment "

#     form_class = AnswerForm
#     template_name = "assessment/quiz.html"

#     def get(self, request, *args, **kwargs):
#         questions = Question.objects.all()
#         return render(request, self.template_name, {'questions' : questions})
    
#     def post(self, request, *args, **kwargs):
#         score = 0
#         for q in Question.objects.all():
#             select_option_id = request.POST.get(f'q_{q.id}')
#             if select_option_id:
#                 select_option = Choice.objects.get(pk=select_option_id)
#                 if select_option.correct:
#                     score += 1

#         return render(request, 'assessment/score.html', {'score' : score})


# class TextquizView(View):

#     " Generate score for particular assessment "

#     form_class = AnswerForm
#     template_name = "assessment/text_quiz.html"

#     def get(self, request, *args, **kwargs):
#         # if Assesment.objects.exists() == True:
#         #     print()
#         assesment = Assessment.objects.last()
#         questions = assesment.question_set.all()
#         count = questions.count()
#         user = request.user
#         print("=================", user)
#         if count == 0:
#             return HttpResponse('assessment doesnt have question now')
#         else:
#             AnswerFormSet = modelformset_factory(Answer, form = AnswerForm, extra = count)
#             formset = AnswerFormSet(queryset = Answer.objects.none())
#             questions = Question.objects.all()
#             return render(request, self.template_name, {'questions' : questions, 'formset' : formset, 'assesment': assesment})

#     def post(self, request, *args, **kwargs):
#         assesment = Assessment.objects.last()
#         questions = assesment.question_set.all()
#         count = questions.count()
#         # user = request.user
#         AnswerFormSet = modelformset_factory(Answer, form = AnswerForm, extra = count)
#         formset = AnswerFormSet(request.POST, queryset = Answer.objects.none())
#         # formset = formset.forms.user == user
#         if formset.is_valid():
#             formset.save()
#             return HttpResponse('added')
        
#         return HttpResponse('not added')
    

class ShowQuizView(View):

    " Showing quiz according to user request "

    def get(self, request, *args, **kwargs):
        assessment = Assessment.objects.get(id = self.kwargs['pk'])
        if assessment.type == 'mcq':
            questions = assessment.question_set.all()
            return render(request, 'assessment/quiz.html', {'questions' : questions,
                                                            'assessment' : assessment,})
        else:
            questions = assessment.question_set.all()
            count = questions.count()
            user = request.user.id
            print(user)
            AnswerFormSet = modelformset_factory(Answer, form = AnswerForm, extra = count)
            # AnswerFormSet.form = staticmethod(curry(AnswerForm, user=request.user.id))
            formset = AnswerFormSet(queryset = Answer.objects.none())
            return render(request, 'assessment/showquiz.html', {'questions' : questions, 
                                                                 'formset' : formset,
                                                                 'user' : user,
                                                                 'assessment' : assessment,})
                                                                 
        
    def post(self, request, *args, **kwargs):
        assessment = Assessment.objects.get(id = self.kwargs['pk'])
        if assessment.type == 'mcq':
            score = 0
            for q in Question.objects.all():
                select_option_id = request.POST.get(f'q_{q.id}')
                if select_option_id:
                    select_option = Choice.objects.get(pk=select_option_id)
                    if select_option.correct:
                        score += 1
            return render(request, 'assessment/score.html', {'score' : score})
        else:
            questions = assessment.question_set.all()
            count = questions.count()
            AnswerFormSet = modelformset_factory(Answer, form = AnswerForm, extra = count)
            # AnswerFormSet.form = staticmethod(curry(AnswerForm, user=request.user.id))
            formset = AnswerFormSet(request.POST, queryset = Answer.objects.none())
            print(formset.errors)
            if formset.is_valid():
                formset.save()
                return HttpResponse('added')

            return HttpResponse('not added')