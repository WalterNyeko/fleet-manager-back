from rest_framework import serializers
from .models import VehicleInPull

class VehicleInPullSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VehicleInPull
        fields = ('in_pull_name','created_on')