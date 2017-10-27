"""
poolapp URL Configuration

"""
from django.conf.urls import url, include
from django.contrib import admin

from applications.accounts.views import FacebookLogin

urlpatterns = [
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^rest-auth/facebook/$', FacebookLogin.as_view(), name='fb_login'),
    url(r'^admin/', admin.site.urls),
    # url(r'^accounts/', include('allauth.urls')),
]
