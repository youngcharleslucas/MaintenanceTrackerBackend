from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from vehicle.models import Vehicle
from vehicle.serializers import VehicleSerializer
from .models import OperatorVehicle
from .serializers import OperatorVehicleSerializer
from django.contrib.auth import get_user_model
from django.apps import apps

User = get_user_model()


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_operator_vehicle(request):
    operator_vehicle = OperatorVehicle.objects.all()
    serializer = OperatorVehicleSerializer(operator_vehicle, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_operator_vehicle(request):
    print(request.user.id)
    # operator_vehicle = OperatorVehicle.objects.filter(operator = request.user.id)
    # vehicles = Vehicle.objects.filter(operator_vehicle.id)

    
    my_ve = Vehicle.objects.filter(operatorvehicle__operator__id=request.user.id)

    results = [item for item in my_ve]


    # vehicle = operator_vehicle.filter(vehicle_id = operator_vehicle.vehicle_id)
    serializer = VehicleSerializer(my_ve, many=True)
    return Response(serializer.data)


# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def get_operator_vehicle(request):
#     print(request.user.id)
#     operator_vehicle = OperatorVehicle.objects.filter(user = request.user.id)
     
#     serializer = OperatorVehicleSerializer(operator_vehicle, many=True)
#     return Response(request.data)



# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def get_operator_vehicle(request):

#     print('User', f"{request.user.id} {request.user.email} {request.user.first_name}")

#     if request.method =='POST':
#         serializer = OperatorVehicleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(user=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def get_operator_vehicle(request):

#     print('User', f"{request.user.id} {request.user.email} {request.user.first_name}")

#     if request.method =='POST':
#         serializer = OperatorVehicleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(user=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
