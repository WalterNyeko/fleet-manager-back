from rest_framework import serializers
from .models import VehicleTyre

class VehicleTyreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VehicleTyre
        fields = ('tyre_name','created_on')