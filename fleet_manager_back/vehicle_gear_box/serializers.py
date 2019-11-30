from rest_framework import serializers
from .models import VehicleGearBox

class VehicleGearBoxSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VehicleGearBox
        fields = ('gear_box_name','created_on')