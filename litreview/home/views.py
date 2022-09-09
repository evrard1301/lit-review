from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from publication import models as pub_models


class MePage(LoginRequiredMixin, View):
    def get(self, request):
        reviews = pub_models.Review.objects.filter(user=request.user)
        reviews = reviews.order_by('-time_created')

        tickets = pub_models.Ticket.objects.filter(user=request.user)
        tickets = tickets.order_by('-time_created')

        items = []

        for review in reviews:
            items.append({
                'type': 'review',
                'obj': review
            })

        for ticket in tickets:
            items.append({
                'type': 'ticket',
                'obj': ticket
            })

            items = sorted(items,
                           key=lambda x: x['obj'].time_created,
                           reverse=True)

        paginator = Paginator(items, 5)
        total_page = paginator.num_pages
        current_page = int(request.GET.get('page', 1))

        return render(request, 'home/me.html', {
            'user': request.user,
            'items': items,
            'page_itr': range(1, total_page + 1),
            'page': paginator.get_page(current_page),
            'current_page': current_page
        })


class SocialPage(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'home/social.html', {
        })
