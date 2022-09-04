from django import forms
from . import models


class UserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = [
            'username',
            'password',
        ]

        widgets = {
            'password': forms.PasswordInput
        }

    confirm = forms.CharField(max_length=256,
                              required=True,
                              widget=forms.PasswordInput,
                              label="Confirmer le mot de passe")

