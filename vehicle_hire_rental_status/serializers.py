from rest_framework import serializers
from .models import VehicleHireRentalStatus

class VehicleHireRentalStatusSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VehicleHireRentalStatus
        fields = ('vehicle_hire_rental_status', 'created_on')