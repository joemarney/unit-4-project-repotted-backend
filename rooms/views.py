from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from utilities.exceptions import catch_exceptions
from .serializers import RoomSerializer, PopulatedRoomSerializer

from .models import Room

# Create your views here.
class ListCreateRoomView(APIView):

    @catch_exceptions
    def get(self, request):
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)
    
    @catch_exceptions
    def post(self, request):
        request.data['owner'] = request.user.id
        room = RoomSerializer(data=request.data)
        room.is_valid(raise_exception=True)
        room.save()
        return Response(room.data, status.HTTP_201_CREATED)
    
class RetrieveUpdateDestroyRoomView(APIView):

    @catch_exceptions
    def get(self, request, pk):
        room = Room.objects.get(pk=pk)
        serializer = PopulatedRoomSerializer(room)
        return Response(serializer.data)
    
    @catch_exceptions
    def put(self, request, pk):
        room = Room.objects.get(pk=pk)
        self.check_object_permissions(request, room)
        serializer = RoomSerializer(room, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)