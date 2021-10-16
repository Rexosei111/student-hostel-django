from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from .models import User
from django.conf import settings


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = '__all__'


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = '__all__'


class CustomAuthenticationForm(AuthenticationForm):
    def clean(self):
        username = normalize_index_number(self.cleaned_data.get('username'))
        password = self.cleaned_data.get('password')
        self.cleaned_data['username'] = username

        if username is not None and password:
            self.user_cache = authenticate(
                self.request, username=username, password=password)
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)
        print(self.cleaned_data)
        return self.cleaned_data
