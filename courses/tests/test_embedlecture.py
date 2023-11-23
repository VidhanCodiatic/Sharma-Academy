from django.test import TestCase
from courses.tests.factory import CourseFactory, EmbedLectureFactory
from users.tests.factory_user import UserFactory
from faker import Factory


faker = Factory.create()

class EmbedLectureViewTestCase(TestCase):

    def test_create_embedlecture(self):
        instructor = UserFactory()
        course = CourseFactory(instructor=instructor)
        self.assertIsNotNone(course)
        embedlecture = EmbedLectureFactory(instructor=instructor, course=course)
        self.assertIsNotNone(embedlecture)