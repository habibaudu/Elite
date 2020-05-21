from rest_framework import viewsets
from users_app.models import (User)
from users_app.serializer import (RegisterSerializer)
from rest_framework.response import Response 
from rest_framework.status import (HTTP_200_OK, 
                                   HTTP_400_BAD_REQUEST, HTTP_201_CREATED)
from users_app.utils.helpers import (format_response) 


class RegisterViewset(viewsets.ViewSet):
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
            


