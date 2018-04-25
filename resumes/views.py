from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView

from easy_pdf.views import PDFTemplateResponseMixin

from .forms import AwardsFormset, EducationFormset, ExperienceFormset, SkillsFormset
from .models import Awards, Education, Experience, Resume, Skills


@login_required
def resume_builder(request):
    # This view creates a Resume model and its corresponding sections.
    resume, _ = Resume.objects.get_or_create(user=request.user)

    # Filter data from db for models relevant to current user.
    existing_resume_data = {
        'education': Education.objects.filter(resume__user=request.user),
        'experience': Experience.objects.filter(resume__user=request.user),
        'awards': Awards.objects.filter(resume__user=request.user),
        'skills': Skills.objects.filter(resume__user=request.user)
    }

    if request.method == 'POST':
        education_formset = EducationFormset(request.POST, prefix='education', instance=resume)
        experience_formset = ExperienceFormset(request.POST, prefix='experience', instance=resume)
        awards_formset = AwardsFormset(request.POST, prefix='awards', instance=resume)
        skills_formset = SkillsFormset(request.POST, prefix='skills', instance=resume)

        if education_formset.is_valid()\
                and experience_formset.is_valid()\
                and awards_formset.is_valid()\
                and skills_formset.is_valid():

            # Save form!
            education_formset.save()
            experience_formset.save()
            awards_formset.save()
            skills_formset.save()

    education_formset = EducationFormset(prefix='education')
    experience_formset = ExperienceFormset(prefix='experience')
    awards_formset = AwardsFormset(prefix='awards')
    skills_formset = SkillsFormset(prefix='skills')

    return render(request, 'resume-builder.html', {
        'existing': existing_resume_data,
        'formsets': [education_formset, experience_formset, awards_formset, skills_formset],
    })


class ResumeView(PDFTemplateResponseMixin, DetailView):
    model = Resume
    template_name = 'resume.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.request.user
        context['education'] = Education.objects.filter(resume__user=self.request.user)
        context['experience'] = Experience.objects.filter(resume__user=self.request.user)
        context['awards'] = Awards.objects.filter(resume__user=self.request.user)
        context['skills'] = Skills.objects.filter(resume__user=self.request.user)
        return context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ResumeView, self).dispatch(request, *args, **kwargs)
