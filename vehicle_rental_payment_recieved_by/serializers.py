from rest_framework import serializers
from .models import VehicleRentalPaymentRecievedBy

class VehicleRentalPaymentRecievedBySerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VehicleRentalPaymentRecievedBy
        fields = ('vehicle_rental_payment_recieved_by', 'created_on')
