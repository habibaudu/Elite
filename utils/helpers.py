from rest_framework.response import Response 
from django.db import models
from utils.id_genrator import (LENGTH_OF_ID, generate_id)
from utils.enumerators import(StateType)

def format_response(**kwargs):
    if kwargs.get("error"):
        return Response({"error":kwargs.get("error"),**kwargs},
                  status = kwargs.get("status",400))
    return Response({**kwargs},status = kwargs.get("status",200))



class BaseModel(models.Model):
    """ Base  Model """
    id = models.CharField(max_length=LENGTH_OF_ID,
                          primary_key=True, default=generate_id, editable=False)
    
    state = models.CharField(max_length=50,
                             choices=[(state.name, state.value) for state in StateType],
                             default='active')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']
    