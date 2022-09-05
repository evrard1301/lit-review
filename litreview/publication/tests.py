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
