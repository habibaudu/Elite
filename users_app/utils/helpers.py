from rest_framework.response import Response 
from django.db import models
from users_app.utils.id_genrator import (LENGTH_OF_ID, generate_id)
from enum import Enum

def format_response(**kwargs):
    if kwargs.get("error"):
        return Response({"error":kwargs.get("error"),**kwargs},
                  status = kwargs.get("status",400))
    return Response({**kwargs},status = kwargs.get("status",200))

class StateType(Enum):
    active = "active"
    deleted = "deleted"

class RequestStatus(Enum):
    pending = "pending"
    confirmed = "confirmed"
    rejectet = "rejected"


class BaseModel(models.Model):
    """ Base  Model """
    id = models.CharField(max_length=LENGTH_OF_ID,
                          primary_key=True, default=generate_id, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']
    