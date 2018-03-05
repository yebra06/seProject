from __future__ import unicode_literals

from django.urls import reverse
from django.test import Client, TestCase


class TestProfileViews(TestCase):

    def setUp(self):
        self.client = Client()

    def test_sanity(self):
        self.assertEqual(1, 1)

    def test_index_get(self):
        self.assertEqual(self.client.get(reverse('index')).status_code, 200)

    def test_login_get(self):
        self.assertEqual(self.client.get(reverse('login')).status_code, 200)

    def test_signup_get(self):
        self.assertEqual(self.client.get(reverse('signup')).status_code, 200)

    def test_login_required_fail(self):
        # These get requests should fail since client is not authenticated.
        self.assertEqual(self.client.get(reverse('user-profile')).status_code, 302)
        self.assertEqual(self.client.get(reverse('user-info')).status_code, 302)
        self.assertEqual(self.client.get(reverse('logout')).status_code, 302)
