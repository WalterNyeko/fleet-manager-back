from rest_framework import serializers
from .models import VehicleRentalPaymentStatus

class VehicleRentalPaymentStatusSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VehicleRentalPaymentStatus
        fields = ('vehicle_rental_payment_status', 'created_on')
