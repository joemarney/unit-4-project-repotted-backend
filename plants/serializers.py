from rest_framework.serializers import ModelSerializer
from .models import Plant, Wishlist
from users.serializers import UserSerializer

class PlantSerializer(ModelSerializer):
    class Meta:
        model = Plant
        fields = '__all__'

class PopulatedWishlistSerializer(ModelSerializer):
    user = UserSerializer()
    plant = PlantSerializer(many=True)

    class Meta:
        model = Wishlist
        fields = '__all__'