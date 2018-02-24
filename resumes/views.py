from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import EducationFormset, ExperienceFormset

from .models import Resume


@login_required
def resume_builder(request):
    resume = Resume.objects.filter(user=request.user).first()
    if resume is None:
        resume = Resume.objects.create(user=request.user)
    education_formset = EducationFormset(prefix='education')
    experience_formset = ExperienceFormset(prefix='experience')
    if request.method == 'POST':
        education_formset = EducationFormset(request.POST, prefix='education', instance=resume)
        experience_formset = ExperienceFormset(request.POST, prefix='experience', instance=resume)
        if education_formset.is_valid() and experience_formset.is_valid():
            education_formset.save()
            experience_formset.save()
    return render(request, 'resume-builder.html', {
        'education_formset': education_formset,
        'experience_formset': experience_formset,
    })
