from rest_framework import viewsets
from users_app.models import (User)
from network.models import(Connection)
from rest_framework.status import (HTTP_200_OK,
                                   HTTP_400_BAD_REQUEST, HTTP_201_CREATED,
                                   HTTP_404_NOT_FOUND,
                                   HTTP_401_UNAUTHORIZED,
                                   HTTP_500_INTERNAL_SERVER_ERROR)
from utils.helpers import (format_response) 
from utils.enumerators import (RequestStatus)

class ConnectionViewsets(viewsets.ViewSet):

    def create(self, request):
        initiating_user = request.user.id
        target_user = request.data['target_user']

        valid_user = User.objects.filter(id=target_user, is_active=True).first()
        if valid_user is None:
            return format_response(error = 'Target user does not exit',
                                   status = HTTP_404_NOT_FOUND)
        
        if Connection.objects.filter(initiator_id=initiating_user,following_id=target_user)\
                                      or Connection.objects.filter(initiator_id=target_user,following_id=initiating_user):
            return format_response(error="Connection already exist",
                                   status=HTTP_400_BAD_REQUEST)
        elif initiating_user == target_user:
            return format_response(error="You cannot initiate a connection with yourself",
                                   status=HTTP_400_BAD_REQUEST)
        

        Connection.objects.create(initiator_id=initiating_user,
                                               following_id = target_user)

        return format_response(message = 'Connection initiated',
                               status=HTTP_201_CREATED)

    def partial_update(self, request, pk):
        
        try:
            connection = Connection.objects.get(id=pk,request=RequestStatus.pending.value)
        except Connection.DoesNotExist:
            return format_response(error = "Connection instance does not exist",
                                   status = HTTP_404_NOT_FOUND)
        if connection.initiator_id == request.user.id:
            return format_response(error="You cannot accept your own connection request",
                                 status = HTTP_400_BAD_REQUEST)
        
        connection.request = RequestStatus.confirmed.value
        connection.save()
        return format_response(message = "Connection request accepted", 
                               status=HTTP_200_OK)

    def destroy(self, request, pk):
        
        try:
            connection = Connection.objects.get(id=pk,request=RequestStatus.pending.value)
        except Connection.DoesNotExist:
            return format_response(error = "Connection instance does not exist")
        
        if connection.initiator_id == request.user.id:
            return format_response(error="You cannot reject your own connection request")
        
        connection.request = RequestStatus.rejected.value
        connection.save()
        return format_response(message = "Connection request rejected")

  