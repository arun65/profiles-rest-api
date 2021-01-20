from rest_framework import serializers
from profiles_api import models


class HelloSerializer(serializers.Serializer):
    """Serailizers a name field for testing our APIViews"""
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer): # serializer for a model
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile # sets the serializer to point to UserProfile model
        fields = ('id', 'email', 'name', 'password') # the fields which we want to serialize, password is not required to show
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'} # makes input field type as password in browser (shows dots when we type password)
            }
        }
    
    def create(self, validated_data):
        """create and return a new user"""

        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user