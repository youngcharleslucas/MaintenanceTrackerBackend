from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Vehicle
from .serializers import VehicleSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_vehicles(request):
    vehicle = Vehicle.objects.all()
    serializer = VehicleSerializer(vehicle, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_vehicles(request):
    if request.method == 'POST':
        serializer = VehicleSerializer(data=request.data)
        serializer.save()




# class VehicleList(APIView):

#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         vehicle = Vehicle.objects.all()
#         serializer = VehicleSerializer(vehicle, many=True)
#         return Response(serializer.data)