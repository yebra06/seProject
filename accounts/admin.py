from __future__ import unicode_literals

from django.contrib import admin

from .models import Education, Experience, Profile

admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Profile)
