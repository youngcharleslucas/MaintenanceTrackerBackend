from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import MaintenanceItem
from .serializers import MaintenanceItemSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_maintenance_items(request):
    maintenance_item = MaintenanceItem.objects.all()
    serializer = MaintenanceItemSerializer(maintenance_item, many=True)
    return Response (serializer.data)