from django.urls import reverse
from django.test import TestCase, Client
from . import models
from authentication.models import User


class CreateTicketTest(TestCase):
    def test_ok_ticket_without_image(self):
        c = Client()
        User.objects.create_user(username='aze', password='aze')
        c.login(username='aze', password='aze')
        self.assertEquals(0, models.Ticket.objects.count())

        c.post(reverse('tickets'), {
            'title': 'My ticket',
            'description': 'This is my ticket'
        })

        self.assertEquals(1, models.Ticket.objects.count())


class EditTicketTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='alice',
                                             password='azerty')
        self.ticket = \
            models.Ticket.objects.create(title='my ticket',
                                         description='this is my ticket',
                                         user_id=self.user.id)
        self.ticket.save()

        self.client = Client()
        self.client.login(username=self.user.username, password='azerty')

    def test_ok_edit_ticket_title(self):
        self.assertEquals('my ticket', self.ticket.title)

        self.client.post(reverse('edit_ticket',
                                 kwargs={'id': self.ticket.id}), {
            'title': 'I love pizza'
        })

        ticket = models.Ticket.objects.get(id=self.ticket.id)
        self.assertEquals('I love pizza', ticket.title)

    def test_ok_edit_ticket_description(self):
        self.assertEquals('this is my ticket', self.ticket.description)

        self.client.post(reverse('edit_ticket',
                                 kwargs={'id': self.ticket.id}), {
                                     'title': 'my ticket',
                                     'description': 'nothing'
        })

        ticket = models.Ticket.objects.get(id=self.ticket.id)
        self.assertEquals('nothing', ticket.description)

    def test_err_edit_ticket_not_owned(self):
        user = User.objects.create_user(username='bob', password='coucou')
        self.client.login(username=user.username, password='coucou')

        self.assertEquals('my ticket', self.ticket.title)

        self.client.post(reverse('edit_ticket',
                                 kwargs={'id': self.ticket.id}), {
                                     'title': 'my new title',
                                     'description': 'a description'
        })

        ticket = models.Ticket.objects.get(id=self.ticket.id)
        self.assertEquals('my ticket', ticket.title)


class CreateTicketReviewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='alice',
                                             password='azerty')
        self.ticket = \
            models.Ticket.objects.create(title='my ticket',
                                         description='this is my ticket',
                                         user_id=self.user.id)
        self.ticket.save()

        self.client = Client()
        self.client.login(username=self.user.username, password='azerty')

    def test_ok_create_ticket(self):
        self.assertEquals(0, models.Review.objects.count())

        self.client.post(reverse('ticket_review',
                                 kwargs={'id': self.ticket.id}), {
                                     'headline': 'my headline',
                                     'body': 'the body',
                                     'rating': 4
                                 })

        self.assertEquals(1, models.Review.objects.count())
        review = models.Review.objects.all()[0]
        self.assertEquals('my headline', review.headline)
        self.assertEquals('the body', review.body)
        self.assertEquals(4, review.rating)
        self.assertEquals(self.ticket.id, review.ticket.id)
        self.assertEquals(self.user.id, review.user.id)
