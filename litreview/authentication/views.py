from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView, LogoutView
from . import forms


class SignupPage(generic.CreateView):
    form_class = forms.UserForm
    success_url = reverse_lazy('login')
    template_name = 'authentication/signup.html'


class LoginPage(LoginView):
    form_class = forms.LoginForm
    template_name = 'authentication/login.html'
    next_page = reverse_lazy('signup')


class LogoutPage(LogoutView):
    next_page = reverse_lazy('login')
