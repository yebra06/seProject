# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def user_login(request):
    return render(request, 'login.html')


def user_signup(request):
    return render(request, 'signup.html')
