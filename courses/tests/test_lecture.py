from django.test import TestCase
from django.urls import reverse, resolve
from users.models import CustomUser
from users.forms import RegisterForm
from courses.tests.factory_course import CourseFactory
# from django.contrib.auth import get_user_model
from faker import Factory


faker = Factory.create()

# # Create your tests here.


class LectureViewTest(TestCase):

    def setUp(self):
        self.course = CourseFactory()
        pass

    def test_register_success(self):

        print(self.course)