from rest_framework import status
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from maintenance_item.models import MaintenanceItem
from maintenance_item.serializers import MaintenanceItemSerializer
from .models import MaintenanceLog
from .serializers import MaintenanceLogSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

# get all maintenance logs
@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_maintenance_log (request):
    maintenance_log = MaintenanceLog.objects.all()
    serializer = MaintenanceLogSerializer(maintenance_log, many=True)
    return Response(serializer.data)

# get just the MaintenanceItem information for the maintenance log
# @api_view(['GET'])
# @permission_classes([AllowAny])
# def get_maintenance_for_log (request):
# # It will get the MaintenanceItem object that has a value matching the id of 1 in the db table maintenancelog(created as maintenance_log but SQL shortens it) under the field maintenance
#     maintenance_log = MaintenanceItem.objects.filter(maintenancelog__maintenance__id=1)
#     serializer = MaintenanceItemSerializer(maintenance_log, many=True)
#     return Response(serializer.data)

# get the maintenance logs for vehicle id
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_log_for_vehicle (request, id):
    maintenance_logs = MaintenanceLog.objects.filter(vehicle__id= id)
    serializer = MaintenanceLogSerializer(maintenance_logs, many=True)
    return Response(serializer.data)

# get the maintenance items for vehicle id
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_maintenance_item_for_vehicle (request, id):
    # !!!GET maintenance items for vehicle through maintenance log tabel!!!!!!!!
    maintenance_items = MaintenanceItem.objects.filter(maintenancelog__vehicle__id = id)
    serializer = MaintenanceItemSerializer(maintenance_items, many=True)
    return Response(serializer.data)

# get single maintenance log through log id
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_maintenance_log (request, id):
    maintenance_items = MaintenanceLog.objects.filter(id=id)
    serializer = MaintenanceLogSerializer(maintenance_items, many=True)
    return Response(serializer.data)

# Get all maintenance logs that are not complete for vehicle id. These will be the alerts. The log miles for when the maintenance was performed sets the start for when the maintenance will be due next.
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def get_incomplete_logs (request, id):
#     vehicle_logs = MaintenanceLog.objects.filter(vehicle__id=id)
#     incomplete_logs = vehicle_logs.filter(complete = False)
#     serializer = MaintenanceLogSerializer(incomplete_logs, many=True)
#     return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_incomplete_logs (request, id):
    vehicle_logs = MaintenanceLog.objects.filter(vehicle__id=id)
    incomplete_logs = vehicle_logs.exclude(complete = True)
    serializer = MaintenanceLogSerializer(incomplete_logs, many=True)
    return Response(serializer.data)



# GET (not PUT) complete = True for maintenance log by maintenance log id

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_update_complete_true(request, id):
    completed = MaintenanceLog.objects.get(id=id)
    # Updates just the key "complete" to True
    completed.complete = True
    completed.save()
    # Only changed one key, so eliminated many=True. The error was 'MaintenaceLog' object is not iterable, 500
    serializer = MaintenanceLogSerializer(completed)
    return Response(serializer.data)
    
# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def post_new_log(request):
#     serializer = MaintenanceLogSerializer(data=request.data)
#     if serializer.is_valid()






# get the maintenance logs for vehicle id, AllowAny test of the above because React is giving 401 error, Postman worked with above though
# THIS DOES NOT WORK WITH AXIOS!!!!!!!!!! Axios cannot send GET requests information through the body!!!!! You must pass it through the HTTP <str:Value Here>
# @api_view(['GET'])
# @permission_classes([AllowAny])
# def get_log_for_vehicle (request):
#     result = [item for item in request.data]
#     # request.data returns a dictionary (the submitted body in the request is a dictionary). Keys in the data dictionary are accessed by ['key_name'], not .key_name
#     maintenance_logs = MaintenanceLog.objects.filter(vehicle__id=request.data['id'])
#     serializer = MaintenanceLogSerializer(maintenance_logs, many=True)
#     return Response(serializer.data)