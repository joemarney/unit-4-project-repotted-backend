from rest_framework.serializers import ModelSerializer
from .models import Plant, Wishlist

class PlantSerializer(ModelSerializer):
    class Meta:
        model = Plant
        fields = '__all__'

class WishlistSerializer(ModelSerializer):
    # user = UserSerializer()
    # plant = PlantSerializer(many=True)

    class Meta:
        model = Wishlist
        fields = ['id', 'user', 'plant', 'created_at']
        read_only_fields = ['id', 'user', 'created_at']