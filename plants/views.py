from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .serializers import PlantSerializer, WishlistSerializer
from .models import Plant, Wishlist

# Create your views here.
class PlantListView(ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer

class PlantDetailView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer

class WishlistListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WishlistSerializer

    def get_queryset(self):
        queryset = Wishlist.objects.filter(user=self.request.user).select_related('plant')
        return queryset
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class WishlistDestroyView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WishlistSerializer

    def get_queryset(self):
        return Wishlist.objects.filter(user=self.request.user)