from django.db import models

# Create your models here.
class VehicleHireRentalStatus(models.Model):
    vehicle_hire_rental_status = models.CharField(max_length=200)
    created_on =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.vehicle_hire_rental_status
