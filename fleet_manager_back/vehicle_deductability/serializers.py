from rest_framework import serializers
from .models import VehicleDeductability

class VehicleDeductabilitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VehicleDeductability
        fields = ('deductability_name','created_on')