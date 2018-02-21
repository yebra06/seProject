from django.conf import settings
from django.db import models


class Resume(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Experience(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    start_month_year = models.CharField(max_length=4, blank=True)
    end_month_year = models.CharField(max_length=4, blank=True)


class Education(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    school = models.CharField(max_length=255, blank=True)
