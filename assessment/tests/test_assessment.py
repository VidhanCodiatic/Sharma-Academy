from django.test import TestCase
from courses.tests.factory import CourseFactory, LectureFactory
from assessment.tests.factory import AssessmentFactory
from faker import Factory


faker = Factory.create()


class AssessmentViewTestCase(TestCase):

    def test_create_assessment(self):
        course = CourseFactory()
        assessment = AssessmentFactory(course=course)
        self.assertIsNotNone(assessment)