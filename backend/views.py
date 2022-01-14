from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BackendSerializer
from .models import Test

@api_view(["GET"])
def endpoints(request):
    routes=[
        {
            "Endpoint":"/test",
            "method":"GET",
            "body":None,
            "description":"This is a test file"
        }
    ]
    return Response(routes)

@api_view(["GET"])
def access_api(request):
    data=Test.objects.all()
    serializer=BackendSerializer(data,many=True)
    return Response(serializer.data)

# fetch data from id

@api_view(["GET"]) 
def get_by_id(request,pk):
    data=Test.objects.get(id=pk)
    serializer=BackendSerializer(data,many=True)
    return Response(serializer.data)


    
    
                                                                                           