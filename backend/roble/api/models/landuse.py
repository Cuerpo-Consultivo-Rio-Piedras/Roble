from django.contrib.gis.db import models
from api.constants import UseTypes
from api.constants import Municipality
from api.constants import Classifications


class LandUse(models.Model):
    object_id = models.IntegerField()
    type = models.CharField(max_length=1, choices=UseTypes.choices)
    municipality = models.CharField(max_length=255, choices=Municipality.choices)
    clasi_put = models.CharField(max_length=255, choices=Classifications.choices)
    description = models.CharField(max_length=255)
    shape_length = models.FloatField()
    shape_area = models.FloatField()
    geometry = models.GeometryField()