from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^add_book$', views.add_book, name="add_book"),
    path('book_detail/<int:book_id>', views.book_detail, name="book_detail"),
    url(r'^$', views.all_books, name="books"),

    url(r'^add_author', views.add_author, name="add_author"),
    path('authors/<int:author_id>', views.author_detail, name="author_detail"),
    url(r'^authors', views.all_authors, name="authors"),
    path('add_book_to_author', views.add_book_to_author, name="add_book_to_author")
]
