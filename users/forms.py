
from users.models import CustomUser
from django import forms


class RegisterForm(forms.ModelForm):

    class Meta:
        password = forms.CharField(required = False, widget = forms.PasswordInput())
        model = CustomUser
        widgets = {
            'password': forms.PasswordInput(),
            'phone': forms.NumberInput(),
        }
        fields = ['email', 'phone', 'password', 'type']

class LoginForm(forms.ModelForm):

    class Meta:
        password = forms.CharField(widget = forms.PasswordInput())
        model = CustomUser
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = ['email', 'password']