from django.contrib.gis.db import models
# Create your models here.

class Poi(models.Model):

    name = models.CharField(max_length=50)
    location = models.PointField()