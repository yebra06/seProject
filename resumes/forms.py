from django.forms import modelformset_factory, BaseModelFormSet

from .models import Education, Experience


class EducationFormsetCleaner(BaseModelFormSet):
    def clean(self):
        super().clean()
        for form in self.forms:
            school = form.cleaned_data['school'].title()
            form.cleaned_data['school'] = school
            form.instance.school = school


EducationFormset = modelformset_factory(Education, exclude=('resume',), formset=EducationFormsetCleaner)
ExperienceFormset = modelformset_factory(Experience, exclude=('resume',))
