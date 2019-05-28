from django.urls import path
from django.conf.urls import url

from . import views

# Note - if i specify app name, I need to use this format for reverse:
# https://stackoverflow.com/questions/49655525/django-2-0-not-a-valid-view-function-or-pattern-name-customizing-auth-views
# app_name = "tv_app"

urlpatterns = [
    url(r'^new', views.new, name='new'),
    # path('new', views.new, name='new'),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/destroy', views.destroy, name='destroy'),
    path('<int:pk>/update', views.update, name='update'),
]
