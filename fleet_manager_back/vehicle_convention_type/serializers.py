from rest_framework import serializers
from .models import VehicleConventionType

class VehicleConventionTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VehicleConventionType
        fields = ('convention_type_name','created_on')