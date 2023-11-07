from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from assessment.utils import send_email_with_marks
from django.views import View
from django.forms import modelformset_factory
from django.contrib import messages
from django.core.paginator import Paginator
from django.urls import reverse

from assessment.forms import (
    QuestionForm, 
    AnswerForm, 
    AssessmentForm, 
    ChoiceForm, 
    RatingForm
)

from assessment.models import (
    Assessment, 
    Question, 
    Choice, 
    Answer, 
    Rating
)



class ShowAssessmentView(View):

    " Showing all assessment present in project "

    template_name = 'assessment/assessment.html'

    def get(self, request, *args, **kwargs):
        assessment = Assessment.objects.all()
        assessment_per_page = 10
        paginator = Paginator(assessment, assessment_per_page, orphans = 2)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        return render(request, self.template_name, {'assessment' : assessment,
                                                    'page_obj' : page_obj})


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
                messages.success(request, 'form submitted')
                return JsonResponse({'message' : 'form submitted'})
            else:
                return JsonResponse({'message' : 'data is not valid'})
        else:
            return JsonResponse({'message' : 'user is not instructor'})


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
            form = RatingForm
            send_email_with_marks(request, score)
            return render(request, 'assessment/score.html', {'score' : score, 'form' : form,
                                                             'assessment': assessment})
        else:
            questions = assessment.question_set.all()
            count = questions.count()
            AnswerFormSet = modelformset_factory(Answer, form = AnswerForm, extra = count)
            # AnswerFormSet.form = staticmethod(curry(AnswerForm, user=request.user.id))
            formset = AnswerFormSet(request.POST, queryset = Answer.objects.none())
            if formset.is_valid():
                formset.save()
                return HttpResponse('added')

            return HttpResponse('not added')
        

def rating_quiz(request):
    if request.method == 'POST':
        form = RatingForm(request.POST)
        # user = request.POST.get('user')
        # if Rating.objects.filter(user = user).exists():
        #     return HttpResponse('user exists')
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("show-assessment"))
        else:
            return HttpResponseRedirect(reverse("index"))
    

