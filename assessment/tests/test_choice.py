from django.test import TestCase
from assessment.tests.factory import ChoiceFactory, QuestionFactory
from faker import Factory


faker = Factory.create()


class ChoiceViewTestCase(TestCase):

    def test_create_assessment(self):
        question = QuestionFactory()
        choice = ChoiceFactory(question=question)
        self.assertIsNotNone(choice)