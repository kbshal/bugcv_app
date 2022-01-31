from rest_framework.serializers import ModelSerializer
from .models import BackendData
from .models import User
from rest_framework.validators import UniqueTogetherValidator

class BackendSerializer(ModelSerializer):
    class Meta:
        model=BackendData
        fields='__all__'

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

