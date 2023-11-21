from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve
from users.models import CustomUser
from users.forms import RegisterForm
from django.contrib.auth import get_user_model
from faker import Factory
from users.views import (
    RegisterView,
    index,
    LoginView,
    ActivateView,
    logout_view,
)

faker = Factory.create()

# Create your tests here.


class RegisterViewTest(TestCase):
    """Test case for the UserCreate view."""

    def setUp(self):

        self.email = faker.email(),
        self.password = faker.password(),
        self.type = 'instructor',
        self.phone = faker.random_number(10)

        self.user = CustomUser.objects.create(
            email=self.email, password=self.password, type=self.type, phone=self.phone)
        
        print(self.email)

    def test_register_get(self):

        register_url = reverse("register")
        response = self.client.get(register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/registration.html')
        self.assertIn('form', response.context)

    def test_register_post_success(self):

        register_url = reverse("register")
        data = {
            'email': faker.email(),
            'password': faker.password(),
            'type': 'student',
            'phone': faker.random_number(10)

        }

        response = self.client.post(register_url, data)

        self.assertEqual(response.status_code, 302)
        # self.assertEqual(CustomUser.objects.count(), 2)
        self.assertRedirects(response, reverse('login'))

    # def test_create_superuser(self):
    #     CustomUser = get_user_model()

    #     admin_user = CustomUser.objects.create_superuser(
    #         "super@example.com", "betterpassword"
    #     )
    #     self.assertEqual(admin_user.email, "super@example.com")
    #     self.assertTrue(admin_user.is_active)
    #     self.assertTrue(admin_user.is_superuser)

    # def test_register_post_failed(self):

    #     # print(self.email)

    #     register_url = reverse("register")
    #     data = {
    #         'email': faker.text(10),
    #         'password': faker.text(10),
    #         'type': 'student',
    #         'phone': faker.random_number(20)

    #     }
    #     # print(data['email'], '===========')
    #     # print(data)
    #     response = self.client.post(register_url, data)
    #     form = RegisterForm(data)

    #     self.assertTrue(CustomUser.objects.filter(
    #         email=self.email).exists())
    #     self.assertFalse(form.is_valid())
    #     self.assertTrue(form['email'].errors, ['Enter a valid email address.'])
    #     self.assertTrue(form["password"].errors, ["Password must be atleast 8 characters long.",
    #                                               "Password must contain one Upper and lower character.",
    #                                               "Password must contain atleast one digit.",
    #                                               "Password must contain atleast one special char."])
    #     self.assertTrue(form['phone'].errors, ['Ensure this value has at most 12 characters'])
    #     self.assertEqual(response.status_code, 302)



#     def test_logout(self):

#         self.client.login(email=self.email, password=self.password)

#         logout_url = reverse('logout')
#         response = self.client.get(logout_url)

#         self.assertEqual(response.status_code, 302) # 302 is status code for redirect
#         self.assertNotEqual(response.status_code, 404)



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
