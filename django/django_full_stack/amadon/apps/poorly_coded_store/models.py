from django.db import models


class Product(models.Model):
    description = models.CharField(max_length=45)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Order(models.Model):
    quantity_ordered = models.IntegerField()
    total_price = models.DecimalField(decimal_places=2, max_digits=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UserManager(models.Manager):
    @staticmethod
    def extra_validation(post_data):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(post_data['first_name']) < 2:
            errors["first_name"] = "First name must be at least 2 letters"
        if len(post_data['last_name']) < 2:
            errors["last_name"] = "Last name must be at least 2 letters"

        s = set()
        for c in post_data["password"]:
            s.add(c)
        if len(s) < 5:
            errors["password"] = "Your password is bad, pick a better one"

        other_users = User.objects.filter(email=post_data["email"])
        if other_users:
            errors["used_email"] = "This email is already being used"

        return errors


class User(models.Model):
    email = models.CharField(max_length=255)
    password_hash = models.CharField(max_length=1023)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    objects = UserManager()
