from rest_framework import serializers
from .models import VehicleCostCenter

class VehicleCostCenterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VehicleCostCenter
        fields = ('cost_center_name','created_on')