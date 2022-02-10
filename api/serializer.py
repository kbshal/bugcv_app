from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from rest_framework.validators import UniqueTogetherValidator


class UserSerializer(ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

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

class CreateUpdatePatientSerializer(ModelSerializer):

    class Meta:
        model = User

        fields = (
           'patient_name',
           'patient_age',
           'patient_number',
           'patient_address',
           'patient_history',
           

        )
