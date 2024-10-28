from rest_framework import viewsets
from .models import Poi
from .serializers import PoiSerializer 

class PoiViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Poi.objects.all()
    serializer_class = PoiSerializer