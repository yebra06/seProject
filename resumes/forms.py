from django import forms
from django.forms import inlineformset_factory, BaseInlineFormSet

from .choices import MONTHS, YEARS
from .models import Awards, Education, Experience, Resume, Skills

# Formsets


# Todo: Validation on inputs.
class ResumeFormset(BaseInlineFormSet):
    def clean(self):
        super().clean()
        for form in self.forms:
            pass


EducationFormset = inlineformset_factory(
    Resume,
    Education,
    exclude=('resume',),
    extra=0,
    min_num=1,
    max_num=5,
    widgets={
        'school': forms.TextInput(attrs={'placeholder': 'School'}),
        'graduation_year': forms.Select(choices=YEARS),
        'degree': forms.TextInput(attrs={'placeholder': 'Degree Earned'})
    }
)

ExperienceFormset = inlineformset_factory(
    Resume,
    Experience,
    exclude=('resume',),
    extra=0,
    min_num=1,
    max_num=10,
    widgets={
        'company': forms.TextInput(attrs={'placeholder': 'Company'}),
        'title': forms.TextInput(attrs={'placeholder': 'Job Title'}),
        'start_month': forms.Select(choices=MONTHS),
        'start_year': forms.Select(choices=YEARS),
        'end_month': forms.Select(choices=MONTHS),
        'end_year': forms.Select(choices=YEARS)
    }
)

SkillsFormset = inlineformset_factory(
    Resume,
    Skills,
    exclude=('resume',),
    extra=0,
    min_num=1,
    max_num=20,
    widgets={
        'skill': forms.TextInput(attrs={'placeholder': 'Skill Name'})
    }
)

AwardsFormset = inlineformset_factory(
    Resume,
    Awards,
    exclude=('resume',),
    extra=0,
    min_num=1,
    max_num=10,
    widgets={
        'award': forms.TextInput(attrs={'placeholder': 'Award'}),
        'year': forms.Select(choices=YEARS)
    }
)
