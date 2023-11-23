from django.test import TestCase
from assessment.tests.factory import AssessmentFactory, QuestionFactory
from faker import Factory


faker = Factory.create()


class QuestionViewTestCase(TestCase):

    def test_create_assessment(self):
        assessment = AssessmentFactory()
        question = QuestionFactory(assessment=assessment)
        self.assertIsNotNone(question)