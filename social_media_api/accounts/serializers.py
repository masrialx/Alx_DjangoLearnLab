from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

# Get the custom user model
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    # Define password as a write-only field for security
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['username', 'password', 'bio', 'profile_picture']
        extra_kwargs = {
            'password': {'write_only': True},  # Ensure the password is write-only
        }

    def create(self, validated_data):
        # Use create_user to properly handle password hashing
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture', None)
        )
        # Create and return token for the user
        Token.objects.create(user=user)
        return user
