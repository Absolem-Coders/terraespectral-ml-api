from django.db import models

# Create your models here.
# models.py

class Ai(models.Model):
    ore = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.ore
