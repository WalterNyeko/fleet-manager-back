from rest_framework import serializers
from .models import VehicleType

class VehicleTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VehicleType
        fields = ('type_name','created_on')