"""Serializer classes for the User model."""
from rest_framework import serializers
from useraccounts.models import User

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
        fields = ['userId', 'username', 'email', 'password']

    def create(self, validated_data):
        """Create method for creating a User with the validated data."""
        user = User.objects.create_user(
            validated_data["username"],
            validated_data["email"],
            validated_data["password"],
        )
        return user
    