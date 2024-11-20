from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=20)
    direction_facing = models.CharField(max_length=5)
    image = models.URLField(default="https://placehold.co/200x200")
    owner = models.ForeignKey('users.User', related_name='owned_rooms', on_delete=models.CASCADE)

    plants = models.ManyToManyField(
        to='plants.Plant',
        related_name='rooms',
        blank=True
    )

    def __str__(self):
        return self.name