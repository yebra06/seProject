from django.contrib import admin

from .models import Awards, Education, Experience, Resume, Skills


class EducationInline(admin.TabularInline):
    model = Education


class ExperienceInline(admin.TabularInline):
    model = Experience


class AwardsInline(admin.TabularInline):
    model = Awards


class SkillsInline(admin.TabularInline):
    model = Skills


class ResumeAdmin(admin.ModelAdmin):
    inlines = [EducationInline, ExperienceInline, AwardsInline, SkillsInline]


admin.site.register(Resume, ResumeAdmin)
