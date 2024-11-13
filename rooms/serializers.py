from rest_framework.serializers import ModelSerializer
from users.serializers import UserSerializer
from .models import Room

class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class PopulatedRoomSerializer(RoomSerializer):
    owner = UserSerializer()