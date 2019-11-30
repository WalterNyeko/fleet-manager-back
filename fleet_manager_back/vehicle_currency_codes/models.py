from django.db import models

# Create your models here.
class VehicleCurrencyCodes(models.Model):
    currency_codes_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.currency_codes_name