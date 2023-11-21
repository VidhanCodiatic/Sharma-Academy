from django.test import TestCase
from assessment.models import Assessment
from django.urls import reverse, resolve
from assessment.forms import AssessmentForm
from users.models import CustomUser
from courses.models import Course
# from PIL import Image


class CustomUserViewTest(TestCase):
    """Test case for the Assessment."""

    def setUp(self):

        self.email = 'vidhan@yopmail.com'
        self.password = 'Vidhan!@#12345'
        self.type = 'instructor'
        self.phone = 7097656788

        self.name = 'python'

        self.test_user = CustomUser.objects.create_user(
            email=self.email, password=self.password, type=self.type, phone=self.phone)
        
        self.user = self.client.login(email=self.email, password=self.password)
        self.assertTrue(self.user)

        self.course = Course.objects.create(instructor=self.test_user, name=self.name,
                                      image='/home/developer/Downloads/html.png',
                                      duration='6 months', fees=30000, 
                                      description="this is description")
    # def test_t(self):
    #     print(self.course)

    # def test_add_assessment_get(self):

    #     assessment_url = reverse("add-assessment")
    #     response = self.client.get(assessment_url)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'assessment/addassessment.html')
    #     self.assertIn('form', response.context)

    # def test_add_assessment_post_success(self):

    #     assessment_url = reverse("add-assessment")
    #     data = {
    #         'course': self.course.id,
    #         'title': 'basic mcq',
    #         'duration': '0:03:00',
    #         'type': 'mcq'
    #     }
    #     response = self.client.post(assessment_url, data)
    #     form = AssessmentForm(data)

    #     self.assertEqual(response.status_code, 200)
    #     self.assertTrue(form.is_valid())
    #     self.assertEqual(Assessment.objects.count(), 1)

    def test_add_assessment_post_failed(self):

        assessment_url = reverse("add-assessment")
        data = {
            'course': 'java',
            'title': 'basic mcq',
            'duration': '0:03:00',
            'type': 'mcq'
        }
        response = self.client.post(assessment_url, data)
        form = AssessmentForm(data)

        self.assertFalse(form.is_valid())