from django.db import models

# Create your models here.


class Vehicle(models.Model):
    vehicle_name = models.CharField(max_length=60)
    vehicle_model = models.CharField(max_length=60)
    vehicle_make = models.CharField(max_length=60)
    vehicle_type = models.CharField(max_length=60)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.vehicle_name
