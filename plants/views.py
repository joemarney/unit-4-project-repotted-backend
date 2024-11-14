from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .serializers import PlantSerializer
from .models import Plant

# Create your views here.
class PlantListView(ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer

class PlantDetailView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer