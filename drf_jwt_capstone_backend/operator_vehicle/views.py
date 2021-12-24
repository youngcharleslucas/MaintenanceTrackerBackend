from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from vehicle.models import Vehicle
# vehicle.serializers import is importing from a different folder outside of the folder this views.py is in. I thought I had to use ..vehicle.serializer to back out of this folder.
from vehicle.serializers import VehicleSerializer
from .models import OperatorVehicle
from .serializers import OperatorVehicleSerializer
from django.contrib.auth import get_user_model
from authentication.serializers import RegistrationSerializer

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
# The double underscore below is joining multiple tables through variables. Retrieves all Vehicle which have a value in the 
# model OperatorVehicle (MySQL lowercases it, check the database) whose operator (defined in the OperatorVehicle model) has the id of request.user.id. 
# Learn more on docs.djangoproject.com field lookups
    my_ve = Vehicle.objects.filter(operatorvehicle__operator__id=request.user.id)
# results =[] is a way to loop through an object and make it more readable. my_ve was difficult to navigate unless mapped through with results = [item for item in my_ve]
# This is how the double underscore path above was found
    results = [item for item in my_ve]
# vehicle = operator_vehicle.filter(vehicle_id = operator_vehicle.vehicle_id)
    serializer = VehicleSerializer(my_ve, many=True)
    return Response(serializer.data)

# Method to get operators from vehicle ID. Not working yet
@api_view(['GET'])
@permission_classes([AllowAny])
def get_vehicle_operator(request):
    vehicle_operator = User.objects.filter(operatorvehicle__vehicle__id=request.data.id)
    result= [item for item in vehicle_operator]
    serializer = RegistrationSerializer(vehicle_operator, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_vehicle_to_user(request):
        serializer = OperatorVehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status+status.HTTP_400_BAD_REQUEST)