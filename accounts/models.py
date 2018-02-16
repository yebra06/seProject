from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    zipcode = models.CharField(max_length=255, blank=True)


class Experience(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    start_month_year = models.CharField(max_length=4, blank=True)
    end_month_year = models.CharField(max_length=4, blank=True)


class Education(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    school = models.CharField(max_length=255)
