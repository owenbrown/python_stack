from .models import Book, Author

b1 = Book(title="C Sharp", desc="Learn C Sharp the easy way")
b1.save()
b2 = Book(title="Java", desc="Learn Java the easy way")
b2.save()
b3 = Book(title="Python", desc="Learn Python the easy way")
b3.save()
b4 = Book(title="PHP", desc="Learn PHP the easy way")
b4.save()
b5 = Book(title="Ruby", desc="Learn Ruby the easy way")
b5.save()

a1 = Author(first_name="Jane", last_name="Austen")
a1.save()
a2 = Author(first_name="Emily", last_name="Dickinson")
a2.save()
a3 = Author(first_name="Fyodor", last_name="Dostoevksy")
a3.save()
a4 = Author(first_name="William", last_name="Shakespeare")
a4.save()
a5 = Author(first_name="Lau", last_name="Tzu")
a5.save()

b = Book.objects.filter(title="C Sharp")[0]
b.title = "C#"
b.save()

a = Author.objects.get(4)
a.first_name = 'Bill'
a.save()

b1 = Book.objects.first()
b2 = Book.objects.get(2)
b3 = Book.objects.get(3)
b4 = Book.objects.get(4)

a = Author.objects.first()
a.books.add(b1)
a.books.add(b2)
a.save()

a2 = Author.objects.get(2)
a2.books.add(b1)
a2.books.add(b2)
a2.books.add(b3)
a2.save()

a3 = Author.objects.get(3)
for i in range(1,5):
    a3.objects.books.add(Book.objects.get(i))
a3.save()

a4 = Author.objects.get(3)
for i in range(1,5):
    a4.objects.books.add(Book.objects.get(i))
a4.save()

print(b3.authors)
b3.authors.remove(a1)
b3.save()

b2.authors.add(a5)
b2.save()

print(a3.books)
print(b5.authors)

