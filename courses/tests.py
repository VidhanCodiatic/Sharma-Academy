from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve
from courses.views import (
    LectureView, 
    ShowLectureView, 
    EmbedLectureView, 
    DocumentView, 
    PdfView, 
    ShowCourseView
)

from courses.models import (
    Course,
    Lecture,
    EmbedLecture, 
    Pdf,
    Document,
)

# Create your tests here.

class TestUrls(SimpleTestCase):

    def test_addlecture_url_is_resolved(self):
        url = reverse('addlecture')
        self.assertEquals(resolve(url).func.view_class, LectureView)

    def test_addembed_url_is_resolved(self):
        url = reverse('addembed')
        self.assertEquals(resolve(url).func.view_class, EmbedLectureView)

    def test_adddox_url_is_resolved(self):
        url = reverse('adddox')
        self.assertEquals(resolve(url).func.view_class, DocumentView)

    def test_addpdf_url_is_resolved(self):
        url = reverse('addpdf')
        self.assertEquals(resolve(url).func.view_class, PdfView)

    def test_showlectures_url_is_resolved(self):
        url = reverse('showlectures')
        self.assertEquals(resolve(url).func.view_class, ShowLectureView)

    def test_buycourse_url_is_resolved(self):
        url = reverse('buycourse', args = ['2'])
        self.assertEquals(resolve(url).func.view_class, ShowCourseView)

# class TestModels(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         print("setUpTestData: Run once to set up non-modified data for all class methods.")
#         pass

#     def setUp(self):
#         print("setUp: Run once for every test method to setup clean data.")
#         pass

class CourseTestCase(TestCase):

    def setUp(self):
        Course.objects.create(
            instructor = "vidhan", 
            name = "Python",
            image = "imhhh",
            duration = "8776",
            )

    def test_courses(self):
        """Courses added"""
        course = Course.objects.get(name = "Python")
        self.assertEqual(course.func.view_class, 'course is "Python"')