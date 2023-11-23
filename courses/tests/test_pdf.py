

from django.test import TestCase
from courses.tests.factory import CourseFactory, PdfFactory
from users.tests.factory_user import UserFactory
from faker import Factory


faker = Factory.create()

class PdfViewTestCase(TestCase):

    def test_create_embedlecture(self):
        instructor = UserFactory()
        course = CourseFactory(instructor=instructor)
        self.assertIsNotNone(course)
        pdf = PdfFactory(instructor=instructor, course=course)
        self.assertIsNotNone(pdf)