from rest_framework import serializers
from .models import VehicleHireCostCenter

class VehicleHireCostCenterSerializrs(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VehicleHireCostCenter
        fields = ('vehicle_hire_cost_center', 'created_on')
