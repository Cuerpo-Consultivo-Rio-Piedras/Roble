from django.contrib.gis.db import models

#TODO: What else should i add?
class Community(models.Model):

    name = models.CharField(max_length=64)
    geometry = models.GeometryField()