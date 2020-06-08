import jwt
from django.conf import settings
from rest_framework.status import (HTTP_200_OK, HTTP_400_BAD_REQUEST,
                                   HTTP_401_UNAUTHORIZED)
from rest_framework import viewsets
from django.contrib.auth.hashers import check_password
from adminapp.models import Admin
from adminapp.serializer import LoginSerializer
from utils.helpers import format_response
from django.utils import timezone

class AdminLoginViewSet(viewsets.ViewSet):
    permission_classes = ()
    authentication_classes = ()
    serializer_class = LoginSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            return format_response(error=serializer.errors,
                                   status=HTTP_400_BAD_REQUEST)

        password = serializer.data['password']
        username = serializer.data['username']

        admin = Admin.objects.filter(username=username).first()

        if not admin:
            return format_response(error="Invalid username or password",
                                   status=HTTP_401_UNAUTHORIZED)

        valid_password = check_password(password,admin.password)

        if not valid_password:
            return format_response(error="invalid username or password",
                                    status=HTTP_401_UNAUTHORIZED)

        admin.last_login =timezone.now()

        token =jwt.encode(
            {
                "uid":admin.id,
                "iat":settings.JWT_SETTINGS["ISS_AT"](),
                "exp":settings.JWT_SETTINGS["EXP_AT"]()
            },settings.SECRET_KEY)

        return format_response(
                               token=token,
                               message="Your login was successful",
                               role=admin.role.name,
                               status=HTTP_200_OK)