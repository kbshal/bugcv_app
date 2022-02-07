
from django.http import Http404
from .models import BackendData
from rest_framework.decorators import api_view
from .serializer import UserSerializer, BackendSerializer,CreateUserSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser,AllowAny
from django.contrib.auth.models import User


class CreateUserAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = [AllowAny,]


'''
 This function shows us the all the available routes or enpoints 

'''


@api_view(["GET", "POST"])
def list_endpoints(request):
    routes = [
        {
            "Endpoint": "/getdata",
            "method": "GET",
            "body": None,
            "description": "Collect all the information"
        },
        {
            "Endpoint": "/name",
            "method": "GET",
            "body": None,
            "description": "Collect name of person"
        }

    ]
    return Response(routes)


@api_view(["GET", "POST"])
def data(request):
    data = BackendData.objects.all()
    data = BackendSerializer(data, many=True)
    return Response(data.data)


@api_view(["GET"])
def get_by_name(request, pk):
    data = BackendData.objects.get(id=pk)
    if data:
        serializer = BackendSerializer(data, many=False)
        return Response(serializer.data)
    else:
        raise Http404(message={"Error": "Occured"})

# upload data


@api_view(["POST"])
def create_data(request):
    get_data = request.data
    backend_data = BackendData.objects.create(name=get_data['name'])
    serializer = BackendSerializer(backend_data, many=False)
    return Response(serializer.data)

# update the existing data


@api_view(["PUT"])
def update_data(request, pk):
    data = request.data
    backend_data = BackendData.objects.get(id=pk)
    serializer = BackendSerializer(backend_data, data=request.POST)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["DELETE"])
def deletedata(request, pk):
    user = BackendData.objects.get(id=pk)
    user.delete()
    return Response("Data was deleted!")

    #  authentication api starts from here


class UserRecordView(APIView):

    permission_classes = [IsAdminUser]

    def get(self, format=None):
        serializer = UserSerializer(self.request.user)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "error": True,
                "error_msg": serializer.error_messages,
            },
            status=status.HTTP_400_BAD_REQUEST
        )
