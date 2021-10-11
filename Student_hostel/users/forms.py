from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from .models import User
from .utils import normalize_index_number


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('index_number', 'email',)

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.index_number = normalize_index_number(
            self.cleaned_data['index_number'])
        if commit:
            user.save()
        return user


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('index_number', 'email',)

    def save(self, commit=True):
        user = super(CustomUserChangeForm, self).save(commit=False)
        user.index_number = normalize_index_number(
            self.cleaned_data['index_number'])
        if commit:
            user.save()
        return user


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
