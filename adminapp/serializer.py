from rest_framework import serializers, exceptions
from users_app.models import (User)

class LoginSerializer(serializers.Serializer):
    ''' Login Serializer '''

    username = serializers.CharField(max_length=100)
    password = serializers.CharField(min_length=5, max_length=100)

class UsersDetailsSerializer(serializers.ModelSerializer):
    """ User details Serializer """
    class Meta:
        model = User
        fields = ["first_name","last_name","email","created_at","updated_at"]

