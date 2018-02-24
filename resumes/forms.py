from django import forms

from .models import Education, Experience, Resume


EducationFormset = forms.inlineformset_factory(Resume, Education, exclude=('resume',), min_num=1, max_num=5)
ExperienceFormset = forms.inlineformset_factory(Resume, Experience, exclude=('resume',), min_num=1, max_num=10)
