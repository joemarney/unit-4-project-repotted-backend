from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from django.db.models import Q
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from utilities.exceptions import catch_exceptions

from django.contrib.auth import get_user_model, hashers

User = get_user_model()

# Create your views here.
class SignUpView(APIView):

    @catch_exceptions
    def post(self, request):
        user = UserSerializer(data=request.data)
        user.is_valid(raise_exception=True)
        user.save()
        return Response({ 
            'message': 'Registration Successful', 
            'user': user.data 
        })

class SignInView(APIView):

    @catch_exceptions
    def post(self, request):
        username_or_email = request.data['username_or_email']
        password = request.data.get('password')
        user = User.objects.get(Q(username=username_or_email) | Q(email=username_or_email))

        if hashers.check_password(password, user.password):
            token_pair = RefreshToken.for_user(user)
            access_token = token_pair.access_token
            access_token['username'] = user.username
            access_token['avatar'] = user.avatar
            serialized_user = UserSerializer(user)
            return Response({ 
                'user': serialized_user.data,
                'token': str(access_token)
            })
    
        return Response({ 'detail': 'Unauthorized' }, status.HTTP_401_UNAUTHORIZED)