from rest_framework import serializers
from .models import VehicleLocationCode

class VehicleLocationCodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VehicleLocationCode
        fields = ('location_code_name','created_on')