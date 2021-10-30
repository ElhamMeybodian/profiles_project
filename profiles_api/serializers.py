from rest_framework import serializers
from . import models


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    # We can do this by declaring serializers that work very similar to Django's forms.
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """A Serializes a user profile object"""

    # model_serializer used of self model

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        # extra_kwargs --> for extra feature for field
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user."""
        print('validated_data', validated_data)
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}
