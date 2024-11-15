from rest_framework import viewsets
from api.models.transmission import TransmissionLine
from api.serializers.transmission import TransmissionLineSerializer

class TransmissionLineViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = TransmissionLine.objects.all()
    serializer_class = TransmissionLineSerializer