from django.db import models

# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    race = models.CharField(max_length=100)
    age = models.IntegerField()