
from django.urls import path
from courses.views import LectureView, ShowLectureView, EmbedLectureView, DocumentView, PdfView, ShowCourseView, index

urlpatterns = [
    path('addlecture/', LectureView.as_view(), name = 'addlecture'),
    path('addembed/', EmbedLectureView.as_view(), name = 'addembed'),
    path('adddox/', DocumentView.as_view(), name = 'adddox'),
    path('addpdf/', PdfView.as_view(), name = 'addpdf'),
    path('showlectures/', ShowLectureView.as_view(), name = 'showlectures'),
    path('showcourses', ShowCourseView.as_view(), name = 'showcourses'),
    path('index/', index, name = 'index1'),
]