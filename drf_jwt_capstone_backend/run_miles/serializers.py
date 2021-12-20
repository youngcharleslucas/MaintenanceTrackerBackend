from rest_framework import serializers
from .models import RunMiles

class RunMilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RunMiles
        fields = ['id', 'miles_current', 'miles_current_date', 'operator', 'vehicle']