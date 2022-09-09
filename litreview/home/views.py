from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from publication import models as pub_models


class MePage(LoginRequiredMixin, View):
    def get(self, request):
        reviews = pub_models.Review.objects.filter(user=request.user)
        reviews = reviews.order_by('-time_created')

        tickets = pub_models.Ticket.objects.filter(user=request.user)
        tickets = tickets.order_by('-time_created')

        return render(request, 'home/me.html', {
            'user': request.user,
            'reviews': reviews,
            'tickets': tickets
        })


class SocialPage(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'home/social.html', {
        })

