from .models import Poi
from rest_framework import serializers

class PoiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poi
        fields = "__all__"