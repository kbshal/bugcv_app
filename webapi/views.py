from .serializers import UserSerializer,DoctorSerializer,PatientHistorySerializer,DoctorSerializer
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .perms import ISDoctor
from django.http import JsonResponse



class CreateUser(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ("post",)
    def create(self,request,*args,**kwargs):
        serializer = super().get_serializer_class()(data=request.data)
        if serializer.is_valid():
            token = Token.objects.get(user=serializer.save())
            return Response({"token":token.key})
        return Response(serializer.errors)


class CreateDoctor(CreateUser):
    serializer_class = DoctorSerializer

class Profile(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request,*args,**kwargs):
        user = request.user
        if not user.is_staff:
            type = "Patient"
        else:
            type = "Doctor"
        return Response({"username":user.username,"email":user.email,"type":type})


class PatientHistoryView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request,*args,**kwargs):
        if request.user.is_staff:
            history = request.user.patientHistory.all()
        else:
            history = request.user.history.all()

        serializer = PatientHistorySerializer(history,many=True)
        for i in serializer.data:
            i["doctor"]=User.objects.get(id=i["doctor"]).get_full_name()
            i["patient"]=User.objects.get(id=i["patient"]).get_full_name()
       


        return Response(serializer.data)
#only doctor is allowed to create patient report

class CreatePatientHistory(ModelViewSet):
    permission_classes = (ISDoctor,)
    serializer_class = PatientHistorySerializer
    http_method_names = ("post",)
    
    def create(self,request,*args,**kwargs):
        serializer = self.serializer_class(data=request.data,context=request)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

def get_info_by_id(request,id):
   try:
       doctor_info=User.objects.get(id=id,is_staff=True)
   except User.DoesNotExist:
        return JsonResponse({"error":"doctor does not exist"})
   info=DoctorSerializer(doctor_info)
   return JsonResponse(info.data)

   

