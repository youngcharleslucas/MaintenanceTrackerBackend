from django.db.models import fields
from rest_framework import serializers
from .models import MaintenanceItem

class MaintenanceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceItem
        fields = ['id', 'maintenance_name', 'maintenance_description', 'maintenance_miles', 'maintenance_periodicity', 'vehicle_type']