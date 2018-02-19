from __future__ import unicode_literals

from django.test import TestCase

from .models import Profile


class ProfileTestCase(TestCase):

    def setUp(self):
        Profile.objects.create(
            email='test1@hotmail.com',
            first_name='First1',
            last_name='Last1',
            street='100 West Ave',
            city='Austin',
            state='tx',
            zipcode='78039')

    def test_profile_address(self):
        profile = Profile.objects.get(email='test1@hotmail.com')
        self.assertEqual(profile.address, '100 West Ave, Austin, TX, 78039')
