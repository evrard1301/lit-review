from django import forms
from . import models


class CreateTicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = ['title', 'description', 'image']
        labels = {
            'title': 'Titre'
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = ['headline', 'body', 'rating']
