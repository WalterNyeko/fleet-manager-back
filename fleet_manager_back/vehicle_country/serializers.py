from rest_framework import serializers
from .models import VehicleCountry

class VehicleCountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VehicleCountry
        fields = ('country_name','created_on')