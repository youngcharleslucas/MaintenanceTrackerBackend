from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class OperatorVehicle(models.Model):
    operator = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle = models.ForeignKey('vehicle.Vehicle', on_delete=models.CASCADE)

