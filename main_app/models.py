from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class hero(models.Model):
    name = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    race = models.CharField(max_length=100)
    age = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
