from rest_framework import serializers
from .models import OperatorVehicle


class OperatorVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperatorVehicle
        fields = ['id', 'operator', 'vehicle']