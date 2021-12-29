from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Vehicle
from .serializers import VehicleSerializer
from django.http import Http404
from django.contrib.auth import get_user_model

User = get_user_model()


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_vehicles(request):
    vehicle = Vehicle.objects.all()
    serializer = VehicleSerializer(vehicle, many=True)
    return Response(serializer.data)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_vehicle(request):
    serializer = VehicleSerializer( data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Get single vehicle with id
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_vehicle(request, id):
    # The id variable was added in urls.py, at the end of the path as <str:id>
    vehicle = Vehicle.objects.filter(id=id)
    # I forgot many=True, the error said 'QuerySet object has no attribute 'vin' and serializer field might be named incorrectly.
    serializer = VehicleSerializer(vehicle, many=True)
    return Response(serializer.data)

# Update miles on vehicle with id
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_miles(request, id):
    # There was an error when filtering without .first(). 'QuerySet' object has no attribute '_meta'. This was because the queryset was returning  a list of records instead of an instance. 
    miles = Vehicle.objects.filter(id=id).first()
    serializer = VehicleSerializer(miles, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def user_vehicles(request):
#     if request.method == 'POST':
#         serializer = VehicleSerializer(data=request.data)
#         serializer.save()




# class VehicleList(APIView):

#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         vehicle = Vehicle.objects.all()
#         serializer = VehicleSerializer(vehicle, many=True)
#         return Response(serializer.data)