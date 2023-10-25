

from django.shortcuts import render, redirect, HttpResponse

from users.forms import RegisterForm, LoginForm
from enrollment.forms import EnrollForm
from django.contrib.auth.hashers import make_password, check_password
from users.models import CustomUser
from courses.models import Course, Lecture
from django.views import View
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings

from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import login, authenticate  , get_user_model
from django.contrib.sites.shortcuts import get_current_site  
from django.utils.encoding import force_bytes, force_str 
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.template.loader import render_to_string  
# from users.tokens import account_activation_token  
from django.core.mail import EmailMessage  
# from .tokens import account_activation_token





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
            user.email_verified = False

            email = user.email
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.id))
            user.save()
            breakpoint()
            send_mail_after_registration(email, uid, token)
            return redirect("/")
        else:
            return HttpResponse('Form is not valid')

    
class LoginView(View):
    form_class = LoginForm
    template_name = "users/login.html"

    def get(self, request, *args, **kwargs):
        login_form = self.form_class()
        return render(request, self.template_name, {"login_form" : login_form })

    def post(self, request, *args, **kwargs):

        login_form = self.form_class()
        payload = request.POST
        email = payload.get('email', '')
        user_password = payload.get('password', '')
        user = authenticate(email = email, password = user_password)

        if user is None:
            messages.success(request, 'Wrong password or email.')
            return redirect('/')
        self.template_name = "users/index.html"
        return render(request, self.template_name, {"login_form" : login_form })
    


@login_required
def index(request):
    enroll_form = EnrollForm
    courses = Course.objects.all()
    users = CustomUser.objects.all()
    upload_video = Lecture.objects.all()
    return render(request, 'users/index.html', {'courses' : courses,
                                                'users' : users,
                                                'upload_video' : upload_video,
                                                'enroll_form' : enroll_form})



def send_mail_after_registration(email, uid, token):
    subject = 'Your accounts need to be verified'
    message = f'Hi paste the link to verify your account http://127.0.0.1:8000/verify/{uid}/{token}/'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message , email_from ,recipient_list )



def verify(request, uidb64, token):
    try:
        breakpoint()
        uid = urlsafe_base64_decode(uidb64).decode()
        print('uid:', uid)
        user = CustomUser.objects.get(pk = uid)
    except(TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None
    print(user)
    print(token)
    print(default_token_generator.check_token(user, token))
    if user is not None and default_token_generator.check_token(user, token):
        user.email_verified = True
        user.save()
        return redirect('/')
    else:
        return HttpResponse('invalid activation')




# def verify_email(request, token):
#     CustomUser = get_user_model()  
#     try:
#         # uid = force_str(urlsafe_base64_decode(uidb64))
        
#         # user = CustomUser.objects.get(pk = request.GET['id'])
#         user = CustomUser.objects.get(pk = uidb64)

#     except(TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
#         return HttpResponse("invalid thing")
    
#     if default_token_generator.check_token(user, token):
#         user.email_verified = True
#         user.save()
#         return HttpResponse('success page')
#     else:
#         return HttpResponse('invalid token page')


    





# def activate(request, uidb64, token):  
#     CustomUser = get_user_model()  
#     try:  
#         uid = force_str(urlsafe_base64_decode(uidb64))  
#         user = CustomUser.objects.get(pk=uid)  
#     except(TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):  
#         user = None  
#     if user is not None and account_activation_token.check_token(user, token):  
#         user.is_active = True  
#         user.save()  
#         return HttpResponse('Thank you for your email confirmation. Now you can login your account.')  
#     else:  
#         return HttpResponse('Activation link is invalid!')  



# import json
# from authlib.integrations.django_client import OAuth
# from django.conf import settings
# from django.shortcuts import redirect, render
# from django.urls import reverse
# from urllib.parse import quote_plus, urlencode
# # from auth0.v3.authentication import GetToken
# # from auth0.v3.management import Auth0

# oauth = OAuth()

# oauth.register(
#     "auth0",
#     client_id=settings.AUTH0_CLIENT_ID,
#     client_secret=settings.AUTH0_CLIENT_SECRET,
#     client_kwargs={
#         "scope": "openid profile email",
#     },
#     server_metadata_url=f"https://{settings.AUTH0_DOMAIN}/.well-known/openid-configuration",
# )


# def authlogin(request):
#     return oauth.auth0.authorize_redirect(
#         request, request.build_absolute_uri(reverse("callback"))
#     )


# def callback(request):
#     token = oauth.auth0.authorize_access_token(request)
#     request.session["user"] = token
#     # code = request.GET['code']
#     # auth0 = Auth0(settings.AUTH_DOMAIN, settings.AUTH0_CLIENT_ID, settings.AUTH0_CLIENT_SECRET)
#     # token_info = GetToken(settings.AUTH_DOMAIN).authorization_code(settings.AUTH0_CLIENT_ID, code, settings.AUTH0_CALLBACK_URL)
#     # access_token = token_info['access_token']
#     # user_info = auth0.users.get(access_token)

#     # print(user_info)
#     # print(request.session.get("user"))
#     user = request.session.get("user").copy()
#     user_info = user.get('userinfo')

#     email = user_info.email
#     print(email)

#     if CustomUser.objects.filter(email = email).exists():
#     # print(user_info)
#     # print(request.session.get("user_userinfo"))
#         return redirect(request.build_absolute_uri(reverse("user_detail")))
#     else:
#         CustomUser.objects.create(email = email)
#         return redirect(request.build_absolute_uri(reverse("user_detail")))



# def authlogout(request):
#     request.session.clear()

#     return redirect(
#         f"https://{settings.AUTH0_DOMAIN}/v2/logout?"
#         + urlencode(
#             {
#                 "returnTo": request.build_absolute_uri(reverse("user_detail")),
#                 "client_id": settings.AUTH0_CLIENT_ID,
#             },
#             quote_via=quote_plus,
#         ),
#     )


# def user_detail(request):
#     return render(
#         request,
#         "users/user_detail.html",
#         context={
#             "session": request.session.get("user"),
#             "pretty": json.dumps(request.session.get("user"), indent=4),
#         },
#     )