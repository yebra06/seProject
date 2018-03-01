from django import forms
from django.forms import inlineformset_factory

from .models import Awards, Education, Experience, Resume, Skills

# Formsets

# Todo: Validation on inputs.
# Todo: Dropdowns maybe?


EducationFormset = inlineformset_factory(
    Resume, Education, exclude=('resume',), extra=0, min_num=1, max_num=5, widgets={
        'school': forms.TextInput(attrs={'placeholder': 'School'}),
        'graduation_year': forms.TextInput(attrs={'placeholder': 'Graduation Year'}),
        'degree': forms.TextInput(attrs={'placeholder': 'Degree Earned'})})

ExperienceFormset = inlineformset_factory(
    Resume, Experience, exclude=('resume',), extra=0, min_num=1, max_num=10, widgets={
        'company': forms.TextInput(attrs={'placeholder': 'Company'}),
        'title': forms.TextInput(attrs={'placeholder': 'Job Title'}),
        'start_month_year': forms.TextInput(attrs={'placeholder': 'Start Month/Year'}),
        'end_month_year': forms.TextInput(attrs={'placeholder': 'End Month/Year'})})

SkillsFormset = inlineformset_factory(
    Resume, Skills, exclude=('resume',), extra=0, min_num=1, max_num=20, widgets={
        'skill': forms.TextInput(attrs={'placeholder': 'Skill Name'})})

AwardsFormset = inlineformset_factory(
    Resume, Awards, exclude=('resume',), extra=0, min_num=1, max_num=10, widgets={
        'award': forms.TextInput(attrs={'placeholder': 'Award'}),
        'year': forms.TextInput(attrs={'placeholder': 'Year Received'})})
