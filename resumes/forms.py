from django.forms import inlineformset_factory

from .models import Awards, Education, Experience, Resume, Skills


EducationFormset = inlineformset_factory(Resume, Education, exclude=('resume',), extra=1, min_num=1, max_num=5)
ExperienceFormset = inlineformset_factory(Resume, Experience, exclude=('resume',), extra=1, min_num=1, max_num=10)
SkillsFormset = inlineformset_factory(Resume, Skills, exclude=('resume',), extra=1, min_num=1, max_num=20)
AwardsFormset = inlineformset_factory(Resume, Awards, exclude=('resume',), extra=1, min_num=1, max_num=10)
