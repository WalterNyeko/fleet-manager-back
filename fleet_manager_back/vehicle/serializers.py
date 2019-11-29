from rest_framework import serializers
from .models import Vehicle
from vehicle_tyre.serializers import VehicleTyreSerializer


class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    vehicle_tyre = VehicleTyreSerializer(many=False, read_only=True)
    class Meta:
        model = Vehicle
        fields = ('id', 'registration_no', 'vehicle_type',
                  'vehicle_make', 'created_on', 'vehicle_tyre')
