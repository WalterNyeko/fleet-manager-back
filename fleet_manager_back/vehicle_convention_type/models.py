from django.db import models

# Create your models here.
class VehicleConventionType(models.Model):
    convention_type_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.convention_type_name