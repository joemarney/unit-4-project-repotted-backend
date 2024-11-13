from django.urls import path
from .views import ListCreateRoomView

urlpatterns = [
    path('', ListCreateRoomView.as_view())
]