from django.db import models


class CourseManager(models.Manager):
    def extra_validation(self, post_data):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(post_data['name']) < 2:
            errors["name"] = "course name should be at least 2 characters"
        if len(post_data['description']) < 15:
            errors["description"] = "description should be at least 15 characters"
        if "orange" in post_data["description"]:
            errors["orange"] = "i don't like the word orange"

        return errors


class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()
