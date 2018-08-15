from __future__ import unicode_literals

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import LoginForm, SignupForm, UserForm
from resumes.models import Resume


def index(request):
    return render(request, 'index.html')


def user_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST or None)
        if form.is_valid():
            account = authenticate(
                username=form.cleaned_data['email'],
                password=form.cleaned_data['password'])
            if account is not None:
                if account.is_active:
                    login(request, account)
                    return redirect('index')
            else:
                form.add_error(None, 'Your email or password is incorrect.')
    return render(request, 'user-login.html', {'form': form})


def user_signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            account = authenticate(username=user.username, password=password)
            login(request, account)
            return redirect('user-info')
    return render(request, 'user-signup.html', {'form': form})


@login_required
def user_profile(request):
    return render(request, 'user-profile.html', {
        'user': request.user,
        'resume': Resume.objects.get(user=request.user) if Resume.objects.filter(user=request.user).exists() else None
    })


@login_required
def user_info(request):
    form = UserForm(instance=request.user)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = form.cleaned_data.get('first_name').capitalize()
            user.last_name = form.cleaned_data.get('last_name').title()
            user.street = form.cleaned_data.get('street').title()
            user.city = form.cleaned_data.get('city').title()
            user.state = form.cleaned_data.get('state').title()
            user.save()
            return redirect('user-profile')
    return render(request, 'user-info.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('index')
