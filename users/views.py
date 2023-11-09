

from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect

from users.models import CustomUser
from courses.models import Course, Lecture
from assessment.models import Assessment
from users.forms import RegisterForm, LoginForm
# from enrollment.forms import EnrollForm
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, get_user_model
from django.conf import settings

from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from users.tokens import email_verification_token

from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.contrib.auth import logout


User = settings.AUTH_USER_MODEL


class RegisterView(View):

    """ User registration with mail confirmation """

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
            user.is_active = False

            user.save()
            current_site = get_current_site(self.request)
            subject = 'Activate Your Account'
            body = render_to_string(
                'users/email_verification.html',
                {
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': email_verification_token.make_token(user),
                }
            )
            EmailMessage(to=[user.email], subject=subject, body=body).send()
            messages.success(request, 'verify your email.')
            return redirect("/")
        else:
            messages.success(
                request, 'Please check email/phone | User already exists.')
            return redirect("/register/")


class LoginView(View):

    """ Login here via email and password """

    form_class = LoginForm
    template_name = "users/login.html"

    def get(self, request, *args, **kwargs):
        login_form = self.form_class()
        return render(request, self.template_name, {"login_form": login_form})

    def post(self, request, *args, **kwargs):

        login_form = self.form_class()
        payload = request.POST
        email = payload.get('email', '')
        user_password = payload.get('password', '')
        user = authenticate(email=email, password=user_password)
        if user is None:
            messages.success(
                request, 'Please verify email or check email / password')
            return redirect('/')
        else:
            login(request, user)
            return redirect('/index/')


@login_required
def index(request):
    courses = Course.objects.all()
    assessments = Assessment.objects.all()
    users = CustomUser.objects.all()
    upload_video = Lecture.objects.all()
    return render(request, 'users/index.html', {'courses': courses,
                                                'users': users,
                                                'upload_video': upload_video,
                                                'assessments': assessments,
                                                })


class ActivateView(View):

    """ User's email verification """

    def get_user_from_email_verification(self, uid, token: str):
        try:
            uid = force_str(urlsafe_base64_decode(uid))
            user = get_user_model().objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError,
                get_user_model().DoesNotExist):
            return None

        if user is not None \
                and \
                email_verification_token.check_token(user, token):
            return user
        else:
            return None

    def get(self, request, uidb64, token):
        user = self.get_user_from_email_verification(uidb64, token)
        user.is_active = True
        user.save()
        return HttpResponseRedirect(reverse('login'))

    


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))



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
