from django.shortcuts import render


def resume_builder(request):
    return render(request, 'resume-builder.html', {})
