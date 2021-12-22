from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class MaintenanceItem (models.Model):
    maintenance_name = models.CharField(max_length=100)
    maintenance_miles = models.IntegerField(blank=True)
    maintenance_periodicity = models.CharField(max_length=20, blank=True)
    maintenance_description = models.CharField(max_length=300)
    vehicle_type = models.ManyToManyField('vehicle.VehicleType')
    # vehicle_type = models.ForeignKey('vehicle.VehicleType', null=True, on_delete=models.SET_NULL)



    # VEHICLE_TYPE_CHOICES = [
    #     (1, 'Car'),
    #     (2, 'Motorcycle')
    # ]
    # vehicle_type = models.IntegerField(choices=VEHICLE_TYPE_CHOICES, default=1, unique=True)

    def __str__(self) -> str:
        return self.maintenance_name

    #vehicle_type changes to manytomany field, uses 'vehicles.VehicleType' as model
    # Use admin interface or postman to create some maintenance items
    # maintenance_item.MaintenanceItem.vehicle_id