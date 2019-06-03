from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    # I think the line below might be the source of my troubles.
    path('<int:user_id>/wall', views.wall, name='wall'),

    url(r'^login$', views.login, name="login"),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^register$', views.register, name="register"),
    url(r'^message$', views.message, name="message"),
    path('message/<int:message_id>/delete', views.delete_message, name="delete_message"),
    path('message/<int:message_id>/delete', views.delete_message, name="delete_message"),
    # creating a view of a message would be useful for sharing
    url(r'^comment$', views.comment, name="comment"),
    path('comment/<int:comment_id>/delete', views.delete_comment, name="delete_comment"),
]
