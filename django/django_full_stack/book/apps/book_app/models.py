from django.db import models


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    # liked_books = a list of books a given user liked
    # books_uploaded = a list of books uploaded by a given user


class Book(models.Model):
    title = models.CharField(max_length=255)
    uploaded_by = models.ForeignKey(User, related_name='books_uploaded', on_delete='SET_NULL')
    users_who_like = models.ManyToManyField(User, related_name='liked_books')