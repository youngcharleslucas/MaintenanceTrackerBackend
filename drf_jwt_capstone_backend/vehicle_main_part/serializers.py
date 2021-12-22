from rest_framework import serializers
from .models import VehicleMainPart

class VehicleMainPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleMainPart
        fields = ['id', 'vehicle', 'maintenance_id', 'main_part_name', 'main_part_description']
