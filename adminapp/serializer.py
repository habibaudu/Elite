from rest_framework import serializers, exceptions

class LoginSerializer(serializers.Serializer):
    ''' Login Serializer '''

    username = serializers.CharField(max_length=100)
    password = serializers.CharField(min_length=5, max_length=100)