from django.forms import modelformset_factory, BaseModelFormSet, inlineformset_factory, BaseInlineFormSet

from .models import Education, Experience


class EducationFormsetCleaner(BaseModelFormSet):
    def clean(self):
        super().clean()
        for form in self.forms:
            school = form.cleaned_data['school'].title()
            form.cleaned_data['school'] = school
            form.instance.school = school


EducationFormset = modelformset_factory(Education, exclude=('resume',), formset=EducationFormsetCleaner, max_num=10)
ExperienceFormset = modelformset_factory(Experience, exclude=('resume',))
