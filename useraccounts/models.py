"""A subpackage providing additional fields to the User model."""
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator, MinLengthValidator


class User(AbstractUser):
    """Class representing an abstraction of the django-auth model, User.
    
    This subpackage defines a custom User model, named User, which extends
    Django's built-in AbstractUser.

    Attributes
    ----------
    username (CharField):
        A field for storing the username.
    """
    
    # username = models.CharField(
    #     max_length=30, 
    #     unique=True,
    #     validators=[MinLengthValidator(4)])

    def __str__(self):
        """Returns a string representation of the user's username"""
        return str(self.username)
