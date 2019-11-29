from django.db import models

# Create your models here.
class VehicleCountry(models.Model):
    country_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.country_name