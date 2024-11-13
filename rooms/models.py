from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=20)
    direction_facing = models.CharField(max_length=5)
    dependents = models.CharField(blank=True, null=True)
    owner = models.ForeignKey('users.User', related_name='owned_rooms', on_delete=models.CASCADE)

    def __str__(self):
        return self.name