from rest_framework import serializers
from .models import VehicleClient

class VehicleClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VehicleClient
        fields = ('client_name','created_on')