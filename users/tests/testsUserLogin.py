from django.test import TestCase
from users.models import CustomUser
from django.urls import reverse
from users.tests.testsRegister import RegisterViewTest
from faker import Factory
faker = Factory.create()

class UserLoginViewTest(RegisterViewTest):
    """User login for commomly used"""

    def setUp(self):
        print(self.user, "+++++==========")
        
    def test_login(self):

        print(self.a)

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