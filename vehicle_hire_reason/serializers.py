from rest_framework import serializers
from .models import VehicleHireReason

class VehicleHireReasonSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VehicleHireReason
        fields = ('vehicle_hire_reason', 'created_on')