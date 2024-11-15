from django.contrib.gis.db import models
# from api.constants import Municipality


class StreetSegment(models.Model):
    segment_id = models.FloatField()
    fe_name = models.CharField()
    geometry = models.GeometryField()