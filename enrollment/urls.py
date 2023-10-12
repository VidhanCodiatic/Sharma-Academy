from django.urls import path
from enrollment.views import EnrollView

urlpatterns = [
    path('enroll/', EnrollView.as_view(), name = 'enroll'),
]