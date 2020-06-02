from network.models import  (Connection)
from users_app.models import (User)
from rest_framework import exceptions, serializers

class ConnectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Connection
        fields = [
            'initiator',
            'following',
            'request',
            'created_at',
            'updated_at'
        ]

