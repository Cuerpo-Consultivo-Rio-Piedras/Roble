from api.models.street import StreetSegment
from rest_framework import serializers

class StreetSegmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreetSegment
        fields = "__all__"