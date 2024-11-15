from api.models.landuse import LandUse
from rest_framework import serializers

class LandUseSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandUse
        fields = "__all__"