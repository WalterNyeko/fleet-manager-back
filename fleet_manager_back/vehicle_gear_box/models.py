from django.db import models

# Create your models here.
class VehicleGearBox(models.Model):
    gear_box_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.gear_box_name