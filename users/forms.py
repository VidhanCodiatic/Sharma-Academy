
from users.models import CustomUser
from django import forms


class RegisterForm(forms.ModelForm):

    class Meta:
        password = forms.CharField(widget = forms.PasswordInput())
        model = CustomUser
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = ['email', 'phone_number', 'password', 'user_type']

class LoginForm(forms.ModelForm):

    class Meta:
        password = forms.CharField(widget = forms.PasswordInput())
        model = CustomUser
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = ['email', 'password']