from rest_framework import viewsets
from users_app.models import (User)
from network.models import(Connection)
from network.serializer import(ConnectionSerializer)
from rest_framework.status import (HTTP_200_OK,
                                   HTTP_400_BAD_REQUEST, HTTP_201_CREATED,
                                   HTTP_404_NOT_FOUND,
                                   HTTP_401_UNAUTHORIZED)
from users_app.utils.helpers import (format_response) 

class ConnectionViewsets(viewsets.ViewSet):
    serializer_class = ConnectionSerializer()

    def create(self, request):
        initiating_user = request.user.id
        target_user = request.data['target_user']

        valid_user = User.objects.filter(id=target_user, is_active=True).first()
        if valid_user is None:
            return format_response(message = 'Target User does not exit',
                                   status = HTTP_404_NOT_FOUND)

        Connection.objects.create(initiator_id=initiating_user,
                                               following_id = target_user)

        return format_response(message = 'Connection initiated',
                               status=HTTP_201_CREATED)