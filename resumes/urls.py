from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^resume-builder/$', views.resume_builder, name='resume-builder'),
]
