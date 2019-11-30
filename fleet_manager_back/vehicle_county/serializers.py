from rest_framework import serializers
from .models import VehicleCounty

class VehicleCountySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VehicleCounty
        fields = ('county_name','created_on')