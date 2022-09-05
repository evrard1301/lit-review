from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from . import forms
from . import models


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
