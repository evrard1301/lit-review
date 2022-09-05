from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from . import forms
from . import models
from authentication.models import User


class TicketPage(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'publication/ticket.html', {
            'form': forms.CreateTicketForm()
        })

    def post(self, request):
        form = forms.CreateTicketForm(request.POST, request.FILES)

        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('tickets')

        return render(request, 'publication/ticket.html', {
            'form': form
        })


class EditTicketPage(LoginRequiredMixin, View):
    def get(self, request, id):
        form = forms.CreateTicketForm(instance=models.Ticket.objects.get(id=id))
        return render(request, 'publication/edit_ticket.html', {
            'form': form
        })

    def post(self, request, id):
        instance = models.Ticket.objects.get(id=id)
        form = forms.CreateTicketForm(request.POST,
                                      request.FILES,
                                      instance=instance)
        if request.user.id != instance.user_id:
            return render(request, 'publication/edit_ticket.html', {
                'form': form,
                'error': 'impossible de modifier ce ticket'
            })

        if form.is_valid():
            form.save()
            return redirect('login')

        return render(request, 'publication/edit_ticket.html', {
            'form': form
        })


class CreateTicketReview(LoginRequiredMixin, View):
    def get(self, request, id):
        ticket = get_object_or_404(models.Ticket, id=id)
        author = User.objects.get(id=ticket.user_id)
        form = forms.ReviewForm()

        return render(request, 'publication/ticket_review.html', {
            'ticket': ticket,
            'author': author,
            'form': form
        })

    def post(self, request, id):
        ticket = get_object_or_404(models.Ticket, id=id)
        author = User.objects.get(id=ticket.user_id)
        form = forms.ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.ticket = ticket
            review.user = request.user
            review.save()
            return redirect('login')

        return render(request, 'publication/ticket_review.html', {
            'ticket': ticket,
            'author': author,
            'form': form
        })
