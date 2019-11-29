from django.db import models

# Create your models here.
class VehicleHireStatus(models.Model):
    vehicle_hire_status = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.vehicle_hire_status

