from django.urls import path
from .views import ListCreateRoomView, RetrieveUpdateDestroyRoomView

urlpatterns = [
    path('', ListCreateRoomView.as_view()),
    path('<int:pk>/', RetrieveUpdateDestroyRoomView.as_view())
]