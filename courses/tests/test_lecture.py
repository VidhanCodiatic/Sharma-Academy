import factory
from django.test import TestCase
from courses.tests.factory import CourseFactory, LectureFactory
from users.tests.factory_user import UserFactory
from courses.forms import LectureForm
from faker import Factory


faker = Factory.create()


class LectureViewTestCase(TestCase):

    def test_create_lecture(self):
        
        instructor = UserFactory()
        course = CourseFactory(instructor=instructor)
        self.assertIsNotNone(course)
        lecture = LectureFactory(instructor=instructor, course=course)
        self.assertIsNotNone(lecture)

    def test_create_lecture_fail(self):

        instructor = UserFactory()
        course = CourseFactory(instructor=instructor)
        # lecture = LectureFactory(instructor=instructor, course=course)
        data = {
            'instructor': instructor,
            'course': course,
            'title' : faker.text(10),
            'duration': '02:00',
            'lecture': factory.django.FileField(filename='test_lecture.mp4')
        }
        # self.assertTrue(lecture)
        form = LectureForm(data)
        self.assertFalse(form.is_valid())
        # self.assertTrue(form['type'].errors, ['Enter a valid user type.'])





    # def setUp(self):
    #     pass
        # Create a test user with 'instructor' type
        # self.user = CustomUser.objects.create_user(username='testuser', password='testpassword')
        # self.user.type = 'instructor'
        # self.user.save()
        # self.user = UserFactory()

        # # Initialize RequestFactory
        # self.factory = RequestFactory()

    

    # def test_get_method(self):
    #     # Create a GET request to the view
    #     request = self.factory.get(reverse('addlecture'))
    #     request.user = self.user

    #     # Call the view
    #     response = LectureView.as_view()(request)

    #     # Check if the response is successful (status code 200)
    #     self.assertEqual(response.status_code, 200)
    #     # Add more assertions if needed

    # def test_post_method_as_instructor(self):
    #     # Create a POST request to the view
    #     request = self.factory.post(reverse('addlecture'), data={})
    #     request.user = self.user

    #     # Call the view
    #     response = LectureView.as_view()(request)

    #     # Check if the lecture is added successfully for instructor
    #     self.assertEqual(response.status_code, 302)  # Redirect status code
    #     # Add more assertions if needed

    # def test_post_method_as_non_instructor(self):
    #     # Create a non-instructor user
    #     # non_instructor = CustomUser.objects.create_user(username='noninstructor', password='testpassword')

    #     non_instructor = UserFactory(type='student')
    #     # Create a POST request to the view with a non-instructor user
    #     request = self.factory.post(reverse('addlecture'), data={})
    #     request.user = non_instructor

    #     # Call the view
    #     response = LectureView.as_view()(request)

    #     # Check if non-instructor is redirected due to permission error
    #     self.assertEqual(response.status_code, 302)  # Redirect status code
    #     # Add more assertions if needed