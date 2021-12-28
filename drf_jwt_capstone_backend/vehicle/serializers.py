from rest_framework import serializers
from .models import Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['id', 'vin', 'make', 'model', 'trim', 'drive_type', 'vehicle_type', 'miles_current']