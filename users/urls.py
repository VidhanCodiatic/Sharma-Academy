from django.urls import path
from users.views import RegisterView, index, LoginView

urlpatterns = [
    path('', RegisterView.as_view(), name = 'register'),
    path('index/', index, name = 'index'),
    path('login/', LoginView.as_view(), name = 'login'),
]