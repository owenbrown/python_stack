from django.shortcuts import render, redirect
from django.shortcuts import Http404
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Author, Book


def add_book(request):
    assert request.method == 'POST'
    title = request.POST["title"]
    description = request.POST["description"]
    b1 = Book.objects.create(title=title, desc=description)
    b1.save()
    return redirect(to=reverse(all_books))


def book_detail(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        raise Http404("<h1>Not a book</h1>")
    context = dict(book=book, authors=book.authors.all())
    return render(request, "books_authors_app/book_detail.html", context)


def all_books(request):
    print("all_books")
    books = Book.objects.all()
    context = dict(books=books)
    return render(request, template_name="books_authors_app/books.html", context=context)


def add_author(request):
    assert request.method == 'POST'
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    notes = request.POST["notes"]
    a = Author.objects.create(first_name=first_name, last_name=last_name, notes=notes)
    a.save()
    return redirect(to=reverse(all_authors))


def author_detail(request, author_id):
    try:
        author = Author.objects.get(id=author_id)
    except Author.DoesNotExist:
        raise Http404("<h1>Not an author</h1>")

    books = Book.objects.all()

    context = dict(author=author, books=books, authors_books=author.books.all())

    return render(request, "books_authors_app/author_detail.html", context)


def all_authors(request):
    print("all_authors")
    authors = Author.objects.all()
    context = dict(authors=authors)
    return render(request, template_name="books_authors_app/authors.html", context=context)


def add_book_to_author(request):
    print("add book to author")
    assert request.method == "POST"
    author_id = request.POST["author_id"]
    print(author_id)
    try:
        author = Author.objects.get(id=author_id)
    except Author.DoesNotExist:
        raise Http404("Author does not exist")
    print(author)

    book_id = request.POST["book_id"]
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        raise Http404("Book does not exist")

    print("found author, found book")
    author.books.add(book)
    author.save()
    print("successess saving")

    check_reverse = reverse(author_detail, args=[author_id])
    print(check_reverse)

    return redirect(to=reverse(author_detail, args=[author_id]))


