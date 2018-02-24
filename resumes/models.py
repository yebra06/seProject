from django.conf import settings
from django.db import models


class Resume(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class ResumeSection(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Experience(ResumeSection):
    title = models.CharField(max_length=150, blank=False)
    start_month_year = models.CharField(max_length=4, blank=False)
    end_month_year = models.CharField(max_length=4, blank=False)


class Education(ResumeSection):
    school = models.CharField(max_length=255, blank=False)


class Skills(ResumeSection):
    skill = models.CharField(max_length=100, blank=True)


class Awards(ResumeSection):
    award = models.CharField(max_length=255, blank=True)
    year = models.IntegerField(blank=False)