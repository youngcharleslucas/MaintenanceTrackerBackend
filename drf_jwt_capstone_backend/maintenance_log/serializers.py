from rest_framework import serializers
from .models import MaintenanceLog

class MaintenanceLogSerializer(serializers.ModelSerializer):
    # adding as part of depth so that I can include the maintenance item with the log
    # maintenance_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = MaintenanceLog
        # fields = ['id', 'maintenance', 'operator', 'vehicle', 'log_date', 'log_note', 'log_miles', 'complete']
        # add maintenance_id to include a dict of maintenance item
        # fields = ['id', 'maintenance', 'operator', 'vehicle', 'log_date', 'log_note', 'log_miles', 'complete', 'maintenance_id']
        fields = ['id', 'maintenance', 'operator', 'vehicle', 'log_date', 'log_note', 'log_miles', 'complete']
        depth = 1

# I am unable to make a PUT request to create a Log using MaintenanceLogSerializer. I think it is because of depth=1. This creates a serializer that will be used just for creating new logs.
class MaintenanceLogNoDepthSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceLog
        fields = ['id', 'maintenance', 'operator', 'vehicle', 'log_date', 'log_note', 'log_miles', 'complete']