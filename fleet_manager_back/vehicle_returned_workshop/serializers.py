from rest_framework import serializers
from .models import VehicleReturnedWorkshop

class VehicleReturnedWorkshopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VehicleReturnedWorkshop
        fields = ('returned_workshop_name','created_on')