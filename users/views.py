from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from utilities.exceptions import catch_exceptions

from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.
class SignUpView(APIView):

    @catch_exceptions
    def post(self, request):
        user = UserSerializer(data=request.data)
        user.is_valid(raise_exception=True)
        user.save()
        return Response('Registration Successful', user.data)
    
class SignInView(APIView):

    @catch_exceptions
    def post(self, request):
        return Response('SIGNIN HIT')