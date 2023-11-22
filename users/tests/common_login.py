# from django.test import TestCase, SimpleTestCase, Client
# from django.urls import reverse, resolve
# from users.models import CustomUser
# from users.forms import RegisterForm
# from django.contrib.auth import get_user_model
# from faker import Factory
# from users.views import (
#     RegisterView,
#     index,
#     LoginView,
#     ActivateView,
#     logout_view,
# )

# faker = Factory.create()

# # Create your tests here.



# class UserCommonLogin(TestCase):
#     """Test case for the UserCreate view."""

#     @classmethod
#     def setUpClass(cls):
#         super().setUpClass()

#         cls.email = faker.email()
#         cls.password = faker.password()
#         cls.type = 'instructor'
#         cls.phone = faker.random_number(10)

#         cls.user = CustomUser.objects.create_user(
#             email=cls.email, password=cls.password, type=cls.type, phone=cls.phone)
        
#         client = Client()
#         cls.logged_in = client.login(email=cls.user.email, password=cls.password)

    # @classmethod
    # def tearDownClass(cls):

    #     super().tearDownClass()

    #     cls.user.delete()
















# from django.test import TestCase, Client
# from users.models import CustomUser
# from django.urls import reverse
# # from users.tests.common_login import UserCommonLogin
# from users.tests.factory_user import UserFactory
# from faker import Factory
# faker = Factory.create()


# class UserLoginTest(TestCase):

#     def setUp(self):

#         self.user = UserFactory()
#         login_url = reverse('login')
#         self.logged_in = self.client.post(login_url, email=self.user.email, password=self.user.password)

#     def test_login_success(self):
     
#         self.assertTrue(self.logged_in)


# class UserLoginViewTest(UserCommonLogin):
#     """User login for commomly used"""
        
#     def test_login(self):

#         print(self.logged_in)
#         response = self.client.get(reverse('login'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTrue(self.logged_in)
        # self.assertRedirects(response, reverse('index'))

        # print(self.user.email, 'inherit')
        # logged_in = self.client.login(email=self.user.email, password=self.user.password)

        # print(self.email)
        # print(self.password)
        # login_url = reverse('login')
        # data = {
        #     'email' : self.email,
        #     'password' : self.password,
        # }
        # print(data)
        # response = self.client.post(login_url, data)

        # self.assertEqual(response.status_code, 302)
        # self.assertRedirects(response, reverse('index'))