
from users.models import CustomUser
from django import forms
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


class RegisterForm(forms.ModelForm):

    class Meta:
        password = forms.CharField(
            required = False, 
            widget = forms.PasswordInput(),
            min_length=8,
            strip=True
        )
        model = CustomUser
        widgets = {
            'password': forms.PasswordInput(),
            'phone': forms.NumberInput(),
        }
        fields = ['email', 'phone', 'password', 'type']

        def clean_password(self):
            password = self.cleaned_data.get('password')
            try:
                validate_password(password, self.instance)
            except forms.ValidationError as error:

                # Method inherited from BaseForm
                self.add_error('password', error)
            return password

class LoginForm(forms.ModelForm):

    class Meta:
        password = forms.CharField(widget = forms.PasswordInput())
        model = CustomUser
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = ['email', 'password']