from django.test import TestCase, Client
from django.urls import reverse
from authentication import models


class UserConnexion(TestCase):

    def test_ok_signup(self):
        client = Client()
        result = client.post(reverse('signup'), {
            'username': 'alice32',
            'password': '123456'
        })

        self.assertEquals(200, result.status_code)
        self.assertEquals(1, models.User.objects.count())
        self.assertEquals('alice32', models.User.objects.first().username)

    def test_err_signup_missing_password(self):
        client = Client()
        client.post(reverse('signup'), {
            'username': 'alice32'
        })

        self.assertEquals(0, models.User.objects.count())
