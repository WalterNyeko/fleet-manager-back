from django.db import models

# Create your models here.
class VehicleBodyType(models.Model):
    body_type_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body_type_name