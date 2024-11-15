from rest_framework import viewsets
from api.models.street import StreetSegment
from api.serializers.street import StreetSegmentSerializer

class StreetSegmentViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = StreetSegment.objects.all()
    serializer_class = StreetSegmentSerializer