from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"<Book: {self.title}>"


class Author(models.Model):
    last_name = models.CharField(max_length=45)
    first_name = models.CharField(max_length=45)
    books = models.ManyToManyField(Book, related_name="authors")
    notes = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"<Author: {self.first_name} {self.last_name}>"
