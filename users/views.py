from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from django.db.models import Q
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from utilities.exceptions import catch_exceptions

from django.contrib.auth import get_user_model, hashers

User = get_user_model()

def get_token(user):
    token_pair = RefreshToken.for_user(user)
    access_token = token_pair.access_token
    serialized_user = UserSerializer(user)
    access_token['user'] = serialized_user.data
    return str(access_token)

# Create your views here.
class SignUpView(APIView):

    @catch_exceptions
    def post(self, request):
        user = UserSerializer(data=request.data)
        user.is_valid(raise_exception=True)
        new_user = user.save()
        token = get_token(new_user)
        return Response({ 
            'message': 'Registration Successful', 
            # 'user': user.data 
            'token': token
        })

class SignInView(APIView):

    @catch_exceptions
    def post(self, request):
        u_or_e = request.data['username_or_email']
        password = request.data.get('password')
        user = User.objects.get(Q(username=u_or_e) | Q(email=u_or_e))

        if hashers.check_password(password, user.password):
            # token_pair = RefreshToken.for_user(user)
            # access_token = token_pair.access_token
            # serialized_user = UserSerializer(user)
            # access_token['user'] = serialized_user.data
            token = get_token(user)
            return Response({ 
                # 'user': serialized_user.data,
                'token': token
            })
    
        return Response({ 'detail': 'Unauthorized' }, status.HTTP_401_UNAUTHORIZED)