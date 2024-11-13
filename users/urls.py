from django.urls import path
from .views import SignUpView, SignInView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('signup/', SignUpView.as_view()),
    # path('signin/', TokenObtainPairView.as_view())
    path('signin/', SignInView.as_view())
]