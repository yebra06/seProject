from django.contrib import admin

from .models import Education, Experience, Resume


admin.register(Resume)
admin.site.register(Education)
admin.site.register(Experience)
