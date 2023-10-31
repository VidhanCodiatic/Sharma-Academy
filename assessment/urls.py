from django.urls import path
from assessment.views import ShowAssessmentView, QuizView, QuestionView, AssessmentView, ChoiceView, TextquizView, ShowQuizView

urlpatterns = [
    path('show-assessment/', ShowAssessmentView.as_view(), name = 'show-assessment'),
    path('add-assessment/', AssessmentView.as_view(), name = 'add-assessment'),
    path('question/', QuestionView.as_view(), name = 'question'),
    path('choice/', ChoiceView.as_view(), name = 'choice'),
    path('quiz/', QuizView.as_view(), name = 'quiz'),
    path('text-quiz/', TextquizView.as_view(), name = 'text_quiz'),
    path('show-quiz/<str:pk>/', ShowQuizView.as_view(), name = 'show-quiz'),
]