import jwt
from django.conf import settings
from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework.authentication import (
    BaseAuthentication, get_authorization_header)
from users_app.models import User
from utils.helpers import format_response
from adminapp.models import Admin


class JSONWebTokenAuthentication(BaseAuthentication):
    keyword = 'Bearer'

    def authenticate(self, request):
        token = get_authorization_header(request).decode().split()

        if 'Bearer' not in token:
            raise exceptions.AuthenticationFailed(
                {'error': 'Authentication Failed',
                 'message': 'Bearer String Not Set'})

        try:
            payload = jwt.decode(
                token[1], settings.SECRET_KEY, algorithms=['HS256'])
            user = User.objects.filter(id=payload['uid']).first() or Admin.objects.filter(id=payload['uid']).first()
        except jwt.DecodeError:
            raise exceptions.AuthenticationFailed(
                {'error': 'Authentication Failed',
                 'message': 'Cannot validate your access credentials'})
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed(
                {'error': 'Authentication Failed',
                 'message': 'Token has expired'})

        if not user:
            raise exceptions.AuthenticationFailed(
                {'error': 'Authentication Failed',
                 'message': 'Cannot validate your access credentials'})

        if not user.is_active:
            raise exceptions.AuthenticationFailed(
                {'error': 'Authentication Failed',
                 'message': 'User has not been verified'})

        return (user, payload)