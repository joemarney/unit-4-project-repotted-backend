from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    avatar = models.URLField(blank=True, null=True, default='https://placehold.co/60x60')
    dependents = models.CharField(blank=True, null=True, default='no')