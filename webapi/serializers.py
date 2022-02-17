from django.contrib.auth.models import User
from .models import PatientHistory
from rest_framework import serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username","email","password")
        extra_kwargs = {"password":{"required":True},"email":{"required":True}}
class DoctorSerializer(UserSerializer):
    def create(self,validated_data):
        return User.objects.create(**validated_data,is_staff=True)
class PatientHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientHistory
        fields = ("doctor","patient","remark","recorded_on",)
        extra_kwargs= {"doctor":{"required":False},}
    def create(self,validated_data):
        validated_data["doctor"] = self.context.user
        return PatientHistory.objects.create(**validated_data)