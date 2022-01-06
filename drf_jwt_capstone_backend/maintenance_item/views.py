from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from vehicle.models import Vehicle
from vehicle.serializers import VehicleSerializer
from .models import MaintenanceItem
from .serializers import MaintenanceItemSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_maintenance_items(request):
    maintenance_item = MaintenanceItem.objects.all()
    serializer = MaintenanceItemSerializer(maintenance_item, many=True)
    return Response (serializer.data)

# get maintenance items for vehicle from vehicle id
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_vehicle_maintenance_items(request, id):
    vehicle = Vehicle.objects.get(id=id)
    # serializer = VehicleSerializer(vehicle)
    maintenance_item = MaintenanceItem.objects.filter(vehicle_type__id=vehicle.vehicle_type_id)
    serializer = MaintenanceItemSerializer(maintenance_item, many=True)
    return Response (serializer.data)
