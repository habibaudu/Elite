from django.db import models
from users_app.models import (User)
from utils.helpers import (BaseModel)
from utils.enumerators import (StateType, RequestStatus)

class ConnectionManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(state=StateType)

class Connection(BaseModel):
    initiator = models.ForeignKey(User, related_name = 'friendship_creator_set', on_delete = models.CASCADE)
    following = models.ForeignKey(User, related_name = 'friendship_set', on_delete = models.CASCADE)
    request = models.CharField(
                             max_length=50,
                             choices=[(status.name, status.value) for status in RequestStatus],
                             default='pending') 
    
    
    def get_following(self):
        connection = User.objects.filter(email=self.following)
        return connection

    def get_followers(self):
        connection = User.objects.filter(email=self.initiator)
        return connection

