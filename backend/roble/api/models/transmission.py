from django.contrib.gis.db import models
from api.constants import Municipality


# TODO: Verify this!
class TransmissionLine(models.Model):

    fid = models.IntegerField()
    gid = models.IntegerField()
    region = models.CharField(max_length=64, null=True)
    municipality = models.CharField(max_length=255, choices=Municipality.choices)
    major_proj = models.CharField(max_length=252, null=True)
    asset_id = models.IntegerField(null=True)
    short_desc = models.CharField(max_length=5000,null=True)
    planned_cost = models.FloatField(null=True)
    estimated_time = models.FloatField(null=True)
    phase_name = models.CharField(max_length=252)
    fid_1 = models.IntegerField()
    object_id = models.IntegerField()
    circuit1 = models.IntegerField()
    working = models.IntegerField()
    geometry = models.LineStringField()