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
        errors = []

        if form.is_valid():
            if form.cleaned_data['password'] == form.cleaned_data['confirm']:
                form.save()
                return redirect('login')
            else:
                errors.append('Les mots de passe sont différents')

        return render(request, 'authentication/signup.html', {
            'form': form,
            'errors': errors
        })
