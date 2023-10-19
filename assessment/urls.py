from django.urls import path
from assessment.views import QuizView, QuestionView, create_multiple_content

urlpatterns = [
    path('quiz/', QuizView.as_view(), name = 'quiz'),
    path('question/', QuestionView.as_view(), name = 'question'),
    path('multianswer/', create_multiple_content,
    name='create_multiple_content'),
]