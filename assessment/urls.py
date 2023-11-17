
from django.urls import path

from assessment.views import (
    ShowAssessmentView,
    QuestionView,
    QuestionListView,
    QuestionDeleteView,
    AssessmentView,
    ChoiceView,
    ShowQuizView,
    rating_quiz
)

urlpatterns = [
    path('show-assessment/', ShowAssessmentView.as_view(), name='show-assessment'),
    path('add-assessment/', AssessmentView.as_view(), name='add-assessment'),
    path('question/', QuestionView.as_view(), name='question'),
    path('choice/', ChoiceView.as_view(), name='choice'),
    # question crud
    path('show-question/', QuestionListView.as_view(), name='show-question'),
    path('delete-question/<int:pk>/', QuestionDeleteView.as_view(), name='delete-question'),
    # path('quiz/', QuizView.as_view(), name = 'quiz'),
    # path('text-quiz/', TextquizView.as_view(), name = 'text_quiz'),
    path('show-quiz/<str:pk>/', ShowQuizView.as_view(), name='show-quiz'),
    path('rating/', rating_quiz, name='rating'),
]
