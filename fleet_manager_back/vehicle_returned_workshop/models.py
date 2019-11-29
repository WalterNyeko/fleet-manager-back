from django.db import models

# Create your models here.
class VehicleReturnedWorkshop(models.Model):
    returned_workshop_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.returned_workshop_name