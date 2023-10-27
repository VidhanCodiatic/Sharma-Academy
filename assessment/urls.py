from django.urls import path
from assessment.views import QuizView, QuestionView, AssessmentView, ChoiceView, TextquizView

urlpatterns = [
    path('add-assessment/', AssessmentView.as_view(), name = 'add-assessment'),
    path('question/', QuestionView.as_view(), name = 'question'),
    path('choice/', ChoiceView.as_view(), name = 'choice'),
    path('quiz/', QuizView.as_view(), name = 'quiz'),
    path('text-quiz/', TextquizView.as_view(), name = 'text_quiz'),
    # path('multianswer/', create_multiple_content, name='create_multiple_content'),
]