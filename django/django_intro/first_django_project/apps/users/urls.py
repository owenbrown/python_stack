from django.conf.urls import url

from . import views

urlpatterns = [
    url('^register$', views.register),
    url(r'^login$', views.login),
    url(r'^users$', views.users),
]
