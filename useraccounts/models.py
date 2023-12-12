"""User model module providing additional fields to the User model."""
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
from django.core.validators import MinLengthValidator
from uuid import uuid4

class CustomUserModelManager(BaseUserManager):
    """Class for the Manager for User model."""

    def create_user(self, username, email, password=None):
        """Creates a custom user with the following fields."""
        user = self.model(
            username=username,
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password):
        """Creates a superuser using the create_user() method."""
        user = self.create_user(
            username,
            email,
            password = password
        )
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user
    

class User(AbstractUser, PermissionsMixin):
    """Class representing an abstraction of the django-auth model, User.
    
    This subpackage defines a custom User model, named User, which extends
    Django's built-in AbstractUser.

    Attributes
    ----------
    userId (CharField):
        Unique id field using uuid4.
    username (CharField):
        Username field
    email (EmailField):
        Email field.
    """
    userId = models.CharField(
        max_length=40,
        default=uuid4,
        primary_key=True,
        editable=False)
    username = models.CharField(
        max_length=30, 
        unique=True,
        null=False,
        blank=False,
        validators=[MinLengthValidator(4)])
    email = models.EmailField(
        max_length=100,
        unique=True,
        null=False,
        blank=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    active = models.BooleanField(
        default=True)
    is_staff = models.BooleanField(
        default=False)
    is_superuser = models.BooleanField(
        default=False)
    created_on = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True)
    updated_at = models.DateTimeField(
        auto_now=True)
    
    objects = CustomUserModelManager()

    class Meta:
        verbose_name = "Custom User"

    def __str__(self):
        """Returns a string representation of the user's username"""
        return str(self.username)

