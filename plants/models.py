from django.db import models

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
