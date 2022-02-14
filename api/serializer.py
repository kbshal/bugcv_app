from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import Patient
from rest_framework.validators import UniqueTogetherValidator



# for fetching user info 

class UserSerializer(ModelSerializer):
    class Meta:
        model = User

        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
        )
        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=['username', 'email']
            )
        ]
        extra_kwargs = {'username': {'required': False}}


# for creating or registering user

class CreateUserSerializer(ModelSerializer):

    class Meta:
        model = User

        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password',

        )


# patient create update model serializer    

class CreateUpdatePatientSerializer(ModelSerializer):

    class Meta:
        model = Patient

        fields = (
           'patient_age',
           'patient_number',
           'patient_address',
           'patient_history',
           
        )
