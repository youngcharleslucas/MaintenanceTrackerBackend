from django.db import models
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import VehicleMainPart
from .serializers import VehicleMainPartSerializer
from django.contrib.auth import get_user_model

User = get_user_model

@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_vehicle_main_parts(request):
    vehicle_main_part = VehicleMainPart.objects.all()
    serializer = VehicleMainPartSerializer(vehicle_main_part, many=True)
    return Response (serializer.data)