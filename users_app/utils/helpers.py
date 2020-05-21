from rest_framework.response import Response 

def format_response(**kwargs):
    if kwargs.get("error"):
        return Response({"error":kwargs.get("error"),**kwargs},
                  status = kwargs.get("status",400))
    return Response({**kwargs},status = kwargs.get("status",200))
    

