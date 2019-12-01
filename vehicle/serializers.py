from rest_framework import serializers
from .models import Vehicle


class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('id', 'vehicle_name', 'vehicle_type',
                  'vehicle_make', 'vehicle_model', 'created_on')
