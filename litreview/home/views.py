from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from . import models
from publication import models as pub_models
from authentication import models as auth_models


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
        search = request.GET.get('username', '')
        users = auth_models.User.objects.all()
        users = filter(lambda u: u.username[:len(search)] == search, users)

        users = [{
            'user': u,
            'following': models.UserFollows.objects.filter(
                user=request.user,
                followed_user=u
            ).all(),
            'followers': models.UserFollows.objects.filter(
                user=u,
                followed_user=request.user
            ).all()
        } for u in users]

        filtered_users = []

        show_following = request.GET.get('user_filter', '') == 'followings'

        if show_following:
            filtered_users.extend(
                filter(lambda u: len(u['following']) == 1, users)
            )

        show_followers = request.GET.get('user_filter', '') == 'followers'

        if show_followers:
            filtered_users.extend(
                filter(lambda u: len(u['followers']) == 1, users)
            )

        show_others = request.GET.get('user_filter', '') == 'all'

        if show_others or (
                not show_followers and not show_following and not show_others
        ):
            filtered_users = users

        filtered_users = sorted(filtered_users,
                                key=lambda u: u['user'].username)
        return render(request, 'home/social.html', {
            'users': [
                f for f in filtered_users
                if f['user'].id != request.user.id
            ],
            'n_followings': len(
                models.UserFollows.objects.filter(user=request.user)
            ),

            'n_followers': len(
                models.UserFollows.objects.filter(followed_user=request.user)
            )
        })

    def post(self, request):
        followed = get_object_or_404(auth_models.User, id=request.POST['user'])

        follows = models.UserFollows.objects.filter(user=request.user,
                                                    followed_user=followed)

        if len(follows.all()) == 0:
            models.UserFollows.objects.create(user=request.user,
                                              followed_user=followed)
        else:
            for f in follows.all():
                f.delete()

        return redirect('social')


class NewsFeedPage(LoginRequiredMixin, View):
    def get(self, request):
        users = [
            u.followed_user
            for u in models.UserFollows.objects.filter(user=request.user)
        ]

        if request.user not in users:
            users.append(request.user)

        publications = []

        for user in users:
            tickets = pub_models.Ticket.objects.filter(user=user).all()

            for ticket in tickets:
                publications.append({
                    'user': user,
                    'type': 'ticket',
                    'date': ticket.time_created,
                    'data': ticket
                })

            reviews = pub_models.Review.objects.filter(user=user).all()

            for review in reviews:
                publications.append({
                    'user': user,
                    'type': 'review',
                    'date': review.time_created,
                    'data': review
                })

        publications = sorted(publications,
                              key=lambda p: p['date'],
                              reverse=True)

        current_page = int(request.GET.get('page', 1))
        pages = Paginator(publications, 5)

        return render(request, 'home/news_feed.html', {
            'publications': pages.page(current_page),
            'pages': pages.page_range,
            'current_page': current_page
        })
