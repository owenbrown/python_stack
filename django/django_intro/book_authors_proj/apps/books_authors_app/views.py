from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.urls import reverse
from django.shortcuts import Http404, HttpResponse

from .models import Author, Book


def add_book(request):
    # a = reverse(all_books)
    # print(a)
    # print(type(a))

    assert request.method == 'POST'
    title = request.POST["title"]
    description = request.POST["description"]
    b1 = Book.objects.create(title=title, desc=description)
    b1.save()
    print("book added?")
    return redirect(to=reverse(all_books))


def book_detail(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        raise Http404("<h1>Not a book</h1>")
    context = dict(book=book)
    return render(request, "books_authors_app/book_detail.html", context)


def all_books(request):
    books = Book.objects.all()
    context = dict(books=books)
    return render(request, template_name="books_authors_app/books.html", context=context)
