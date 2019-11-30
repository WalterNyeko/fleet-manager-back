from rest_framework import serializers
from .models import VehicleRentalPaymentRecieved

class VehicleRentalPaymentRecievedSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VehicleRentalPaymentRecieved
        fields = ('vehicle_rental_payment_recieved', 'created_on')
