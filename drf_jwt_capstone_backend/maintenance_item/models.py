from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class MaintenanceItem (models.Model):
    # Typeid
    maintenance_name = models.CharField(max_length=100)
    maintenance_miles = models.IntegerField(blank=True)
    maintenance_periodicity = models.CharField(max_length=20, blank=True)
    maintenance_description = models.CharField(max_length=300)