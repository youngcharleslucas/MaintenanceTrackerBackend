from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class MaintenanceLog(models.Model):
    maintenance = models.ForeignKey('maintenance_item.MaintenanceItem', on_delete=models.CASCADE)
    operator = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle = models.ForeignKey('vehicle.Vehicle', on_delete=models.CASCADE)
    log_miles = models.IntegerField()
    log_note = models.CharField(max_length=300)
    log_date = models.DateField()
    # complete will be True after the maintenance is performed next time. Leaving complete False keeps that Alert active. When the maintenance is due, all False complete maintenance items will display as alerts. Maintenance Log maintains record of when it was last performed.
    complete = models.BooleanField(default=False)

    def __int__(self) -> int:
        return self.maintenance