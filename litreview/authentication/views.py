from django.shortcuts import render, redirect
from django.views import View
from . import forms


def login(request):
    return render(request, 'authentication/login.html', {})


class SignupPage(View):
    def get(self, request):
        return render(request, 'authentication/signup.html', {
            'form': forms.UserForm
        })

    def post(self, request):
        form = forms.UserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

        return render(request, 'authentication/signup.html', {
            'form': form
        })
