from rest_framework.serializers import ModelSerializer
from .models import Plant, Wishlist

class PlantSerializer(ModelSerializer):
    class Meta:
        model = Plant
        fields = '__all__'

class WishlistSerializer(ModelSerializer):
    plant = PlantSerializer()

    class Meta:
        model = Wishlist
        fields = '__all__'