from api.models.transmission import TransmissionLine
from rest_framework import serializers

class TransmissionLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransmissionLine
        fields = "__all__"