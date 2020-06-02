from django.db import models
from users_app.models import (User)

from users_app.utils.helpers import (BaseModel, RequestStatus)

class Connection(BaseModel):
    initiator = models.ForeignKey(User, related_name = 'friendship_creator_set', on_delete = models.CASCADE)
    following = models.ForeignKey(User, related_name = 'friendship_set', on_delete = models.CASCADE)
    request = models.CharField(
                             max_length=50,
                             choices=[(status, status.value) for status in RequestStatus],
                             default=RequestStatus.pending) 
