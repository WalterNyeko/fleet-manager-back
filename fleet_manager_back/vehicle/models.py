from django.db import models
from vehicle_tyre.models import VehicleTyre

# Create your models here.


class Vehicle(models.Model):
    registration_no = models.CharField(max_length=60)
    created_on = models.DateTimeField(auto_now_add=True)
    vehicle_tyre = models.ForeignKey(VehicleTyre, on_delete=models.CASCADE)

    def __str__(self):
        return self.registration_no
