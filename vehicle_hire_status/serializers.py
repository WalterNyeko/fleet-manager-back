from rest_framework import serializers
from .models import VehicleHireStatus

class VehicleHireStatusSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VehicleHireStatus
        fields = ('vehicle_hire_status', 'created_on')