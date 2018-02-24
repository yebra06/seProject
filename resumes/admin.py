from django.contrib import admin

from .models import Education, Experience, Resume


class EducationInline(admin.TabularInline):
    model = Education


class ExperienceInline(admin.TabularInline):
    model = Experience


class ResumeAdmin(admin.ModelAdmin):
    inlines = [EducationInline, ExperienceInline]


admin.site.register(Resume, ResumeAdmin)
