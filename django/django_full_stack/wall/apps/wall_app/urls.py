from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    path('wall/<int:pk>', views.wall, name='wall'),

    url(r'^login$', views.login, name="login"),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^register$', views.register, name="register"),
    url(r'^message$', views.register, name="message"),
    # creating a view of a message would be useful for sharing
    url(r'^comment$', views.register, name="comment"),
]
