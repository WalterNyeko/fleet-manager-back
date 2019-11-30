from django.db import models

# Create your models here.
class VehicleLocationCode(models.Model):
    location_code_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.location_code_name