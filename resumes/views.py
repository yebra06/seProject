from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import EducationFormset, ExperienceFormset
from .models import Resume


@login_required
def resume_builder(request):
    education_form = EducationFormset()
    experience_form = ExperienceFormset()
    if request.method == 'POST':
        education_form = EducationFormset(request.POST)
        experience_form = ExperienceFormset(request.POST)
        if education_form.is_valid() and experience_form.is_valid():
            resume = Resume.objects.filter(user=request.user).first()
            if resume is None:
                resume = Resume.objects.create(user=request.user)
            education_instances = education_form.save(commit=False)
            experience_instances = experience_form.save(commit=False)
            for i in education_instances:
                i.resume = resume
                i.save()
            for i in experience_instances:
                i.resume = resume
                i.save()

    context = {
        'education_form': education_form,
        'experience_form': experience_form,
    }

    return render(request, 'resume-builder.html', context)
