from rest_framework import serializers
from .models import VehicleStatus

class VehicleStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VehicleStatus
        fields = ('status_name','created_on')