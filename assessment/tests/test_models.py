from django.test import TestCase, SimpleTestCase
# from django.urls import reverse, resolve
# from assessment.views import (
#     ShowAssessmentView, 
#     AddAssessmentView,
#     AddQuestionView,
#     AddChoiceView,
#     QuestionListView,
#     QuestionDeleteView,
#     QuestionUpdateView,
#     ShowQuizView,
#     rating_quiz,
# )
# # Create your tests here.

# class TestUrls(SimpleTestCase):

#     def test_show_assessment_url_is_resolved(self):
#         url = reverse('show-assessment')
#         self.assertEquals(resolve(url).func.view_class, ShowAssessmentView)

#     def test_add_assessment_url_is_resolved(self):
#         url = reverse('add-assessment')
#         self.assertEquals(resolve(url).func.view_class, AddAssessmentView)

#     def test_add_question_url_is_resolved(self):
#         url = reverse('add-question')
#         self.assertEquals(resolve(url).func.view_class, AddQuestionView)

#     def test_add_choice_url_is_resolved(self):
#         url = reverse('add-choice')
#         self.assertEquals(resolve(url).func.view_class, AddChoiceView)

#     def test_show_question_url_is_resolved(self):
#         url = reverse('show-question')
#         self.assertEquals(resolve(url).func.view_class, QuestionListView)

#     def test_delete_question_url_is_resolved(self):
#         url = reverse('delete-question', args=['2'])
#         self.assertEquals(resolve(url).func.view_class, QuestionDeleteView)

#     def test_update_question_url_is_resolved(self):
#         url = reverse('update-question', args=['2'])
#         self.assertEquals(resolve(url).func.view_class, QuestionUpdateView)

#     def test_show_quiz_url_is_resolved(self):
#         url = reverse('show-quiz', args=['2'])
#         self.assertEquals(resolve(url).func.view_class, ShowQuizView)

#     def test_rating_url_is_resolved(self):
#         url = reverse('rating')
#         self.assertEquals(resolve(url).func, rating_quiz)