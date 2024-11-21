from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, ReadOnlyField
from .models import Plant, Wishlist

class PlantSerializer(ModelSerializer):
    class Meta:
        model = Plant
        fields = '__all__'

class WishlistSerializer(ModelSerializer):
    plant = PrimaryKeyRelatedField(queryset=Plant.objects.all(), write_only=True)
    plant_details = PlantSerializer(source='plant', read_only=True)
    user = ReadOnlyField(source='user.id')
    # user = UserSerializer()
    # plant = PlantSerializer(many=True)

    class Meta:
        model = Wishlist
        fields = ['id', 'user', 'plant', 'plant_details', 'created_at']
        # read_only_fields = ['id', 'user', 'created_at']

    # def to_internal_value(self, data):
    #     if isinstance(data.get('plant'), dict):
    #         data['plant'] = data['plant'].get('id')
    #     return super().to_internal_value(data)

    # def to_representation(self, instance):
    #     print(f'Serializing wishlist: {instance}, plant: {instance.plant}')
    #     return super().to_representation(instance)