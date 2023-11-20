from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve
from users.models import CustomUser
from users.views import (
    RegisterView, 
    index, 
    LoginView, 
    ActivateView, 
    logout_view,
)

# Create your tests here.

class RegisterViewTest(TestCase):
    """Test case for the AuthorCreate view (Created as Challenge)."""

#     def setUp(self):
#         # Create a user
#         test_user = CustomUser.objects.create_user(
#             email='testuser@yopmail.com', password='some_password', type='student')


#         test_user.save()

    def create_user(self, email="testuser@yopmail.com", password='some_password', type='student'):
        return CustomUser.objects.create(email=email, password=password, type=type)

    def test_user_create(self):
        u = self.create_user()
        url = reverse("register")
        response = self.client.get(url)
        self.assertTrue(isinstance(u, CustomUser))

        self.assertEqual(response.status_code, 200)
        self.assertIn(u.email, response.content)

    # def test_whatever_list_view(self):
    #     w = self.create_whatever()
    #     url = reverse("whatever.views.whatever")
    #     resp = self.client.get(url)

    #     self.assertEqual(resp.status_code, 200)
    #     self.assertIn(w.title, resp.content)
        
        
# class TestUrls(SimpleTestCase):

#     def test_register_url_is_resolved(self):
#         url = reverse('register')
#         self.assertEquals(resolve(url).func.view_class, RegisterView)

#     def test_login_url_is_resolved(self):
#         url = reverse('login')
#         self.assertEquals(resolve(url).func.view_class, LoginView)

#     def test_activate_url_is_resolved(self):
#         url = reverse('activate', args = ['1324', '45'])
#         self.assertEquals(resolve(url).func.view_class, ActivateView)

#     def test_index_url_is_resolved(self):
#         url = reverse('index')
#         self.assertEquals(resolve(url).func, index)

#     def test_logout_url_is_resolved(self):
#         url = reverse('logout')
#         self.assertEquals(resolve(url).func, logout_view)

    # def test_delete_question_url_is_resolved(self):
    #     url = reverse('delete-question', args=['2'])
    #     self.assertEquals(resolve(url).func.view_class, QuestionDeleteView)

    # def test_update_question_url_is_resolved(self):
    #     url = reverse('update-question', args=['2'])
    #     self.assertEquals(resolve(url).func.view_class, QuestionUpdateView)

    # def test_show_quiz_url_is_resolved(self):
    #     url = reverse('show-quiz', args=['2'])
    #     self.assertEquals(resolve(url).func.view_class, ShowQuizView)

    # def test_rating_url_is_resolved(self):
    #     url = reverse('rating')
    #     self.assertEquals(resolve(url).func, rating_quiz)