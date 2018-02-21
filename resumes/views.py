from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import EducationFormset, ExperienceFormset


@login_required
def resume_builder(request):
    education_form = EducationFormset()
    experience_form = ExperienceFormset()
    if request.method == 'POST':
        education_form = EducationFormset(request.POST)
        experience_form = ExperienceFormset(request.POST)
        if education_form.is_valid() and experience_form.is_valid():
            education = education_form.save(commit=False)
            experience = experience_form.save(commit=False)
            education.user = request.user
            experience.user = request.user
            education.save()
            experience.save()
    return render(request, 'resume-builder.html', {'education_form': education_form, 'experience_form': experience_form})
