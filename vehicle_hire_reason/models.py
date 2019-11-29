from django.db import models

# Create your models here.
class VehicleHireReason(models.Model):
    vehicle_hire_reason = models.CharField(max_length=300)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.vehicle_hire_reason