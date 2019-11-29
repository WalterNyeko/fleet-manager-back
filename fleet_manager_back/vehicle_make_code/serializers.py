from rest_framework import serializers
from .models import VehicleMakeCode

class VehicleMakeCodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VehicleMakeCode
        fields = ('make_code_name','created_on')