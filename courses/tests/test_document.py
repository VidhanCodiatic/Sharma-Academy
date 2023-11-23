from django.test import TestCase
from courses.tests.factory import CourseFactory, DocumentFactory
from users.tests.factory_user import UserFactory
from faker import Factory


faker = Factory.create()

class DocumentViewTestCase(TestCase):

    def test_create_document(self):
        instructor = UserFactory()
        course = CourseFactory(instructor=instructor)
        self.assertIsNotNone(course)
        document = DocumentFactory(instructor=instructor, course=course)
        self.assertIsNotNone(document)

