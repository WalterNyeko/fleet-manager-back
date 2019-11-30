from rest_framework import serializers
from .models import VehicleRentalDetailHiringDivision

class VehicleRentalDetailHiringDivisionSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VehicleRentalDetailHiringDivision
        fields = ('vehicle_rental_detail_hiring_division', 'created_on')
