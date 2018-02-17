from django.db import models

from accounts.models import Profile


class Experience(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    start_month_year = models.CharField(max_length=4, blank=True)
    end_month_year = models.CharField(max_length=4, blank=True)


class Education(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    school = models.CharField(max_length=255)
