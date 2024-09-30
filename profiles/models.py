from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    This class represents a user profile, extending the default Django User model.

    Attributes:
        user (User): The associated User object for this profile.
        favorite_city (str): The user's favorite city, optional field.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
# go
