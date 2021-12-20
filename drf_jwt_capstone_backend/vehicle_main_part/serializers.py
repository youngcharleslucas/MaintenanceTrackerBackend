from rest_framework import serializers
from .models import VehicleMainPart

class VehicleMainPartSerializer(serializers.Serializer):
    class Meta:
        main = VehicleMainPart
        fields = ['id', 'vehicle', 'maintenance_id', 'main_part_name', 'main_part_description']
