from django.urls import path
from users.views import RegisterView, index, LoginView

urlpatterns = [
    path('', LoginView.as_view(), name = 'login'),
    path('register/', RegisterView.as_view(), name = 'register'),
    path('index/', index, name = 'index'),
]