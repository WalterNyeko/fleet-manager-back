from django.db import models

# Create your models here.
class VehicleRentalRevenueInvoicedBy(models.Model):
    vehicle_rental_revenue_invoiced_by = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.vehicle_rental_revenue_invoiced_by
