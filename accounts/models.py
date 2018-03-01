from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

from resumes.models import Resume


class Profile(AbstractUser):

    # This model inherits from django's built in User model. See docs.
    # This means that email, first_name, and last_name and other attributes.
    # Hence they are not in the implementation.

    phone_number = models.CharField(max_length=20, blank=True)
    street = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    zipcode = models.CharField(max_length=255, blank=True)

    @property
    def address(self):
        return ', '.join([self.street, self.city, self.state + ' ' + self.zipcode])
