
from django.urls import path
from courses.views import LectureView, ShowLectureView

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('addcourse/', LectureView.as_view(), name = 'addcourse'),
    path('showlectures/', ShowLectureView.as_view(), name = 'showlectures'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)