from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from utilities.exceptions import catch_exceptions


# Create your views here.
class ListCreateRoomView(APIView):

    def get(self, request):
        return Response('INDEX HIT')