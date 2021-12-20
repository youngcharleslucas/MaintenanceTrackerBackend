from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE

User = get_user_model

class VehicleMainPart(models.Model):
    vehicle = models.ForeignKey('vehicle.Vehicle', on_delete=CASCADE)
    maintenance_id = models.ForeignKey('maintenance_item.MaintenanceItem', on_delete=CASCADE)
    main_part_name = models.CharField(max_length=50)
    main_part_description = models.CharField(max_length=100) 
