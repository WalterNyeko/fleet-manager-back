from django.db import models

# Create your models here.
class VehicleRentalPaymentRecievedBy(models.Model):
    vehicle_rental_payment_recieved_by = models.CharField(max_length=60)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.vehicle_rental_payment_recieved_by
