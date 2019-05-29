from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/destroy', views.destroy, name='destroy'),
    path('<int:pk>/destroy_confirm', views.destroy_confirm, name='destroy_confirm')
]
