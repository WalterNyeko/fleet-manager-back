from rest_framework import serializers
from .models import VehicleBodyType

class VehicleBodyTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VehicleBodyType
        fields = ('body_type_name','created_on')