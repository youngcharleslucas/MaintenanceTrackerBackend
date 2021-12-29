from rest_framework import serializers
from .models import MaintenanceLog

class MaintenanceLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceLog
        fields = ['id', 'maintenance' 'operator', 'vehicle', 'log_date', 'log_note', 'log_miles', 'complete']
