from django.db import models


class ShowManager(models.Manager):
    def extra_validation(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 2:
            errors["title"] = "show title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "network name should be at last 3 characters"
        if len(postData['description']) < 10:
            errors["description"] = "description shoud be at least 10 characters"
        return errors


class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ShowManager()
