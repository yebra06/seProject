from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^signup/$', views.user_signup, name='signup'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^user-profile/$', views.user_profile, name='user-profile'),
    url(r'^user-info/$', views.user_info, name='user-info'),
]
