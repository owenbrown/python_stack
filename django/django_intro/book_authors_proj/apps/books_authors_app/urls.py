from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^add', views.add_book, name="add_book"),
    # url(r'^detail', views.book_detail, name="book_detail"),
    path('detail/<int:book_id>', views.book_detail, name="book_detail"),
    url(r'^', views.all_books, name="books"),
    url(r'^all', views.all_books, name="books_alternate"),
]
