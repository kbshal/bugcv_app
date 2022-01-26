from email import message
from django.http import Http404
from .models import BackendData
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import BackendSerializer



'''
 This function shows us the all the available routes or enpoints 

'''
@api_view(["GET","POST"])
def list_endpoints(request):
    routes= [
        {
            "Endpoint":"/getdata",
            "method":"GET",
            "body":None,
            "description":"Collect all the information"
        },
        {
             "Endpoint":"/name",
            "method":"GET",
            "body":None,
            "description":"Collect name of person"
        }
        
            ]
    return Response(routes)

@api_view(["GET","POST"])
def data(request):
    data=BackendData.objects.all()
    data=BackendSerializer(data,many=True)
    return Response(data.data)

@api_view(["GET"])
def get_by_name(request,pk):
    data=BackendData.objects.get(id=pk)
    if data:
        serializer=BackendSerializer(data,many=False)
        return Response(serializer.data)
    else:
        raise Http404(message={"Error":"Occured"})

#upload data 

@api_view(["POST"])
def create_data(request):
    get_data=request.data
    backend_data=BackendData.objects.create(name=get_data['name'])
    serializer=BackendSerializer(backend_data,many=False)
    return Response(serializer.data)

# update the existing data

@api_view(["PUT"])
def update_data(request,pk):
    data=request.data
    backend_data=BackendData.objects.get(id=pk)
    serializer=BackendSerializer(backend_data,data=request.POST)
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)


@api_view(["DELETE"])
def deletedata(request,pk):
    user=BackendData.objects.get(id=pk)
    user.delete()
    return Response("Data was deleted!")










