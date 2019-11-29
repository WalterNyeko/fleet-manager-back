from rest_framework import serializers
from .models import VehicleFuelType

class VehicleFuelTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VehicleFuelType
        fields = ('fuel_type_name','created_on')