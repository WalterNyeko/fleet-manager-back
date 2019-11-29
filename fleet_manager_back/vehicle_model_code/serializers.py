from rest_framework import serializers
from .models import VehicleModelCode

class VehicleModelCodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VehicleModelCode
        fields = ('model_code_name','created_on')