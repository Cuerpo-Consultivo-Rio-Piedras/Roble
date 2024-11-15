from django.contrib import admin
from api.models.transmission import TransmissionLine
from api.models.landuse import LandUse
from api.models.street import StreetSegment
from api.models.community import Community

# Register your models here.
models = [
    TransmissionLine,
    Community,
    LandUse,
    StreetSegment
]
admin.site.register(models)