from __future__ import unicode_literals

from django.test import TestCase

from accounts.models import Profile


class ProfileTestCase(TestCase):

    def setUp(self):
        Profile.objects.create(
            email='test1@hotmail.com',
            first_name='first',
            last_name='last',
            street='100 west ave',
            city='new york',
            state='new york',
            zipcode='78039')

    def test_profile_address(self):
        profile = Profile.objects.get(email='test1@hotmail.com')
        self.assertEqual(profile.address, '100 west ave, new york, new york 78039')
