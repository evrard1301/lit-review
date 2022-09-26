from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from . import models


class UserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = models.User


class LoginForm(AuthenticationForm):
    pass
