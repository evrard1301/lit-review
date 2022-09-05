from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from . import forms


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

