from django.conf.urls import url

from . import views

urlpatterns = [
    url('^new$', views.new),
    url(r'^$', views.index),
]
