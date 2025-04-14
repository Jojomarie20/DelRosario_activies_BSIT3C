from django.db import models
from django.db.models.manager import Manager

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    
    objects: Manager = models.Manager()

    def __str__(self) -> str:
        return str(self.username)
