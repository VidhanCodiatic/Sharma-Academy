

from django.shortcuts import render, redirect, HttpResponse

from users.forms import RegisterForm, LoginForm
from enrollment.forms import EnrollForm
from django.contrib.auth.hashers import make_password, check_password
from users.models import *
from courses.models import Course, Lecture
from django.views import View


class RegisterView(View):
    form_class = RegisterForm
    template_name = "users/registration.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(user.password)
            user.save()
            return redirect("/")
        else:
            return HttpResponse('Form is not valid')

        return render(request, self.template_name, {"form": form})
    
class LoginView(View):
    form_class = LoginForm
    template_name = "users/login.html"

    def get(self, request, *args, **kwargs):
        login_form = self.form_class()
        return render(request, self.template_name, {"login_form" : login_form })

    def post(self, request, *args, **kwargs):
        login_form = self.form_class(request.POST)
        email = request.POST['email']
        user_password = request.POST['password']
        if CustomUser.objects.filter(email = email).exists():
            obj = CustomUser.objects.get(email = email)
            password = obj.password
            if check_password(user_password, password):
                return redirect('/index/')
            else:
                return HttpResponse('password is not correct') 
        else:
            return HttpResponse('email is not register')
        
        return render(request, self.template_name, {"login_form" : login_form })




def index(request):
    enroll_form = EnrollForm
    courses = Course.objects.all()
    users = CustomUser.objects.all()
    upload_video = Lecture.objects.all()
    return render(request, 'users/index.html', {'courses' : courses,
                                                'users' : users,
                                                'upload_video' : upload_video,
                                                'enroll_form' : enroll_form})