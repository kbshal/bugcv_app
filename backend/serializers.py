'''Data serializer for team BugCV'''

from rest_framework.serializers import ModelSerializer
from .models import Test


class BackendSerializer(ModelSerializer):
    class Meta:
        model=Test
        fields='__all__'

