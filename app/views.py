# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from .forms import LoginForm, SignupForm


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
    return render(request, 'login.html', {'form': form})


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
            return redirect('index')
    return render(request, 'signup.html', {'form': form})


def profile(request):
    return render(request, 'profile.html')


def user_logout(request):
    logout(request)
    return redirect('index')
