from django.core import validators
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator


User = get_user_model()

class VehicleType(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.name

class Vehicle(models.Model):
    vin = models.CharField(max_length=17, validators=[MinLengthValidator(17)])
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    trim = models.CharField(max_length=20)
    DRIVE_TYPE_CHOICES = [
        ('FWD', 'Front Wheel Drive'),
        ('RWD', 'Rear Wheel Drive'),
        ('AWD', 'All Wheel Drive'),
        ('4x4', 'Four Wheel Drive')
    ]
    drive_type = models.CharField(max_length=3, choices=DRIVE_TYPE_CHOICES, default='FWD')
    vehicle_type = models.ForeignKey(VehicleType, null=True, on_delete=models.SET_NULL)
    # year = models.DateField(blank=True)
    # drivetrain = models.Field.choices(max_length=20)
    # cylinders = models.CharField(max_length=20)
    # engine_size_cc = models.CharField(max_length=20)
    # engine_size_l = models.CharField(max_length=20)
    # engine_config = models.CharField(max_length=20)
    # doors = models.IntegerField()
    # ownership_date = models.DateField(blank=True)
    # init_miles = models.IntegerField(max_length=6, blank=True)
    # plate_number = models.CharField(max_length=8, blank=True)

    def __str__(self) -> str:
        return f'{self.make} {self.model}'

