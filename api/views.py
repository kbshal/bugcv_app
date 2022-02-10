
from django.http import Http404
from rest_framework.decorators import api_view
from .serializer import UserSerializer,CreateUserSerializer,CreateUpdatePatientSerializer
from rest_framework.generics import CreateAPIView,RetrieveUpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser,AllowAny
from django.contrib.auth.models import User
from .models import Patient


# for registering new user

class CreateUserAPIView(CreateAPIView):

    serializer_class = CreateUserSerializer

    def create(self,request,*args,**kwargs):
        try:
            super(CreateAPIView,self).create(request,*args,**kwargs)
            return Response({"User created success":True})
        except Exception:
            return Response({"User created success":False})
        


# for create patient 

class CreatePatientInfo(CreateAPIView):
    serializer_class = CreateUpdatePatientSerializer
    def create(self,request,*args,**kwargs):
        try:
            super(CreatePatientInfo,self).create(request,*args,**kwargs)
            return Response({"Patient Infomation Recorded":True})
        except Exception:
            return Response({"Patient Infomation Recorded":False})
        

    


# for login and retrieving token

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
