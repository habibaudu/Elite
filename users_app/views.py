import jwt
from rest_framework import viewsets
from django.utils import timezone
from django.conf import settings
from users_app.models import (User)
from network.models import (Connection)
from users_app.serializer import (RegisterSerializer, LoginSerializer, 
                                  InventSerializer, UserProfileSerializer)
from django.contrib.auth.hashers import check_password
from rest_framework.status import (HTTP_200_OK, 
                                   HTTP_400_BAD_REQUEST, HTTP_201_CREATED,
                                   HTTP_404_NOT_FOUND,
                                   HTTP_401_UNAUTHORIZED,
                                   HTTP_500_INTERNAL_SERVER_ERROR)
from utils.helpers import (format_response) 



class RegisterViewset(viewsets.ViewSet):
    authentication_classes = ()
    serializer_class = RegisterSerializer
    def create(self, request):
        request_data = request.data 
        serializer = self.serializer_class(data=request_data)

        if not serializer.is_valid():
            return format_response(errors = serializer.errors.get("errors",serializer.errors),
                            status = HTTP_400_BAD_REQUEST)
        serializer.save()
        return format_response(data=serializer.data, 
                               status = HTTP_201_CREATED,
                               message="Your registerition with Invent is successfully")

class LoginViewSet(viewsets.ViewSet):
    authentication_classes = ()
    serializer_class = LoginSerializer
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return format_response(errors =serializer.errors,
                                   status =HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=request.data["email"].lower())
        except User.DoesNotExist:
            return format_response(errors="No account with that email",
                                   status=HTTP_404_NOT_FOUND)

        password_valid = check_password(serializer.data['password'], user.password)

        if not user.is_active:
            return format_response(error='Your account has not been activated',
                                   status=HTTP_400_BAD_REQUEST)

        if not password_valid:
            return format_response(error='Invalid email or password',
                                   status=HTTP_401_UNAUTHORIZED)

        user.last_login = timezone.now()
        user.save()

        token = jwt.encode({
            'uid': user.id,
            'iat': settings.JWT_SETTINGS['ISS_AT'](),
            'exp': settings.JWT_SETTINGS['EXP_AT']()
        }, settings.SECRET_KEY)

        return format_response(token=token, message='Your login was successful',
                               status=HTTP_200_OK)
            

class InventViewset(viewsets.ViewSet):
    serializer_class = InventSerializer
    def create(self,request):
        request_data = request.data
        serializer = self.serializer_class(data=request_data,
                                           context = {"request":request})

        if not serializer.is_valid():
            return format_response(errors=serializer.errors.get("errors",serializer.errors),
                                  status=HTTP_400_BAD_REQUEST)
        return format_response(data=serializer.data,
                               message="you have successfully added an Invention",
                               status=HTTP_201_CREATED)
        

class UserProfileViewSet(viewsets.ViewSet):
    serializer_class = UserProfileSerializer

    def list(self,request):
        queryset = User.objects.filter(id=request.user.id).first()
        serializer = self.serializer_class(queryset,context={'request':request})
        return format_response(data=serializer.data, 
                               message='Successfully retrived your user information',
                               status=HTTP_200_OK)