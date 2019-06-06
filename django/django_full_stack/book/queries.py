from .apps.book_app.models import *

u1 = User.objects.create(first_name='Joey', last_name='Bo')
u1.save()
u2 = User.objects.create(first_name='Jimmy', last_name='Radney')
u2.save()
u3 = User.objects.create(first_name='Greg', last_name='Kraigher')
u3.save()

b1 = Book.objects.create(
    title="How to be friendly",
    uploaded_by=u1,
)
b1.save()

b2 = Book.objects.create(
    title="Whale",
    uploaded_by=u1
)
b2.save()

b3 = Book.objects.create(
    title="1984",
    uploaded_by=u2
)
b3.save()

b4 = Book.objects.create(
    title="Animal Farm",
    uploaded_by=u2
)

b5 = Book.objects.create(
    title='Jurassic Park',
    uploaded_by=u3
)
b5.save()

b6 = Book.objects.create(
    title='Bridgette Jones Diary'
)
b6.save()

u1.liked_books.add(b1)
u1.liked_books.add(b6)
u1.save()

u2.liked_books.add(b1)
u2.liked_books.add(b3)
u2.save()

for b in [b1, b2, b3, b4, b5, b6]:
    u3.liked_books.add(b)
u3.save()

print(b1.users_who_like.all())
print(b1.uploaded_by)
print(b2.users_who_like.all())
print(b2.uploaded_by)



b2.users_who_like.add(u2)
