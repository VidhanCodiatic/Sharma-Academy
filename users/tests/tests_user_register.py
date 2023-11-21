from django.test import TestCase
from users.models import CustomUser
from django.urls import reverse
from faker import Factory
faker = Factory.create()

class UserRegisterView(TestCase):
    """User login for commomly used"""

    def setUp(self):

        self.email = faker.email(),
        self.password = faker.password(),
        self.type = 'instructor'
        self.phone = faker.random_number(10)

        self.test_user = CustomUser.objects.create(
            email=self.email, password=self.password, type=self.type, phone=self.phone)
        print(self.test_user.email)

    # def test_w(self):
    #     print(self.test_user.id)