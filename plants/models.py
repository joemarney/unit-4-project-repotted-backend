from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Plant(models.Model):
    name = models.CharField(max_length=50)
    image = models.URLField(default="https://placehold.co/200x200")
    scientific_name = models.CharField(max_length=50)
    description = models.TextField(max_length=200, blank=True, null=True)
    sunlight = models.CharField(max_length=8)
    watering = models.CharField(max_length=8)
    toxicity = models.CharField(max_length=8)
    difficulty = models.CharField(max_length=8)

    def __str__(self):
        return f'{self.name}'
    
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked_plants')
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)
