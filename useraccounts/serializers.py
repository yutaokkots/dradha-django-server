"""Serializer classes for the User model."""
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.core.validators import EmailValidator, MinLengthValidator, MaxLengthValidator
from django.contrib.auth.password_validation import validate_password
from .models import User

class UserSerializer(serializers.ModelSerializer):
    """Class representing a serializer for the User model."""

    class Meta:
        """ Meta options for the UserSerializer.

        Attributes
        ----------
        model (User): 
            The model associated with this serializer.
        fields (list):
            A list of fields to include in the serialized output.
        """

        model = User
        fields = ['id', 'username']