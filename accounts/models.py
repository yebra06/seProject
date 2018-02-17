from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    zipcode = models.CharField(max_length=255, blank=True)
