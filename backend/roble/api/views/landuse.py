from rest_framework import viewsets
from api.models.landuse import LandUse
from api.serializers.landuse import LandUseSerializer

class LandUseViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = LandUse.objects.all()
    serializer_class = LandUseSerializer